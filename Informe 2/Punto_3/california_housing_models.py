

import argparse
import os
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def build_pipelines(num_cols, cat_cols):
    # Numerical pipeline: impute median, then scale
    num_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    # Categorical pipeline: impute most frequent, then one-hot
    cat_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore", sparse=False))
    ])

    preprocessor = ColumnTransformer(transformers=[
        ("num", num_pipeline, num_cols),
        ("cat", cat_pipeline, cat_cols)
    ])

    return preprocessor

def main(args):
    data_path = Path(args.data)
    if not data_path.exists():
        raise FileNotFoundError(f"Data file not found: {data_path}.\nPlease download 'california_housing.csv' and place it here or provide a correct path.")
    df = pd.read_csv(data_path)
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    target = "median_house_value"
    if target not in df.columns:
        raise ValueError(f"Target column '{target}' not found in dataset. Columns found: {df.columns.tolist()}")

    # Basic info saved
    with open(output_dir / "dataset_info.txt", "w", encoding="utf-8") as f:
        f.write(f"Loaded file: {data_path}\\n")
        f.write(f"Shape: {df.shape}\\n\\n")
        f.write("Columns:\\n")
        for c in df.columns:
            f.write(f"- {c}\\n")

    # Identify categorical and numerical columns
    cat_cols = [c for c in df.columns if df[c].dtype == "object"]
    num_cols = [c for c in df.columns if c not in cat_cols + [target]]

    # Quick save of missing values
    miss = df.isnull().sum()
    miss.to_csv(output_dir / "missing_values.csv")

    # Train/test split
    X = df.drop(columns=[target])
    y = df[target].copy()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    preprocessor = build_pipelines(num_cols, cat_cols)

    # Define model pipelines
    models = {
        "KNN": Pipeline([("pre", preprocessor), ("model", KNeighborsRegressor())]),
        "RandomForest": Pipeline([("pre", preprocessor), ("model", RandomForestRegressor(random_state=42, n_jobs=-1))]),
        "SVR": Pipeline([("pre", preprocessor), ("model", SVR())])
    }

    # Parameter grids for GridSearchCV
    param_grids = {
        "KNN": {
            "model__n_neighbors": [3, 5, 8],
            "model__weights": ["uniform", "distance"],
            "model__p": [1, 2]
        },
        "RandomForest": {
            "model__n_estimators": [100, 200],
            "model__max_depth": [None, 12, 20],
            "model__min_samples_split": [2, 5]
        },
        "SVR": {
            "model__C": [0.1, 1],
            "model__gamma": ["scale", "auto"],
            "model__kernel": ["rbf", "linear"]
        }
    }

    best_estimators = {}
    cv_results_summary = []

    for name in models:
        print(f"Running GridSearchCV for {name} ...")
        gs = GridSearchCV(models[name], param_grids[name], cv=5, scoring="neg_root_mean_squared_error", n_jobs=-1, verbose=0)
        gs.fit(X_train, y_train)
        print(f" Best params {name}: {gs.best_params_}")
        best_estimators[name] = gs.best_estimator_
        cv_rmse = -gs.best_score_
        cv_results_summary.append((name, cv_rmse, gs.best_params_))
        # Save best params for each model
        with open(output_dir / f"best_params_{name}.txt", "w", encoding="utf-8") as f:
            f.write(str(gs.best_params_))
            f.write("\\nCV best RMSE: " + str(cv_rmse))

    # Evaluate on test set and save metrics
    results = []
    for name, model in best_estimators.items():
        y_pred = model.predict(X_test)
        rmse = mean_squared_error(y_test, y_pred, squared=False)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        results.append((name, rmse, mae, r2))
        # Save predictions
        pd.DataFrame({"y_test": y_test, "y_pred": y_pred}).to_csv(output_dir / f"predictions_{name}.csv", index=False)

    results_df = pd.DataFrame(results, columns=["model", "RMSE", "MAE", "R2"]).sort_values("RMSE")
    results_df.to_csv(output_dir / "results.csv", index=False)

    # Plots for best model
    best_name = results_df.iloc[0]["model"]
    best_model = best_estimators[best_name]
    y_pred_best = best_model.predict(X_test)

    plt.figure(figsize=(6,6))
    plt.scatter(y_test, y_pred_best, alpha=0.4)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--")
    plt.xlabel("Valor real")
    plt.ylabel("Valor predicho")
    plt.title(f"Real vs Predicho — {best_name}")
    plt.tight_layout()
    plt.savefig(output_dir / f"real_vs_pred_{best_name}.png", dpi=150)
    plt.close()

    resid = y_test - y_pred_best
    plt.figure(figsize=(6,4))
    sns.histplot(resid, bins=50, kde=True)
    plt.title(f"Residuales — {best_name}")
    plt.xlabel("Residuo (real - predicho)")
    plt.tight_layout()
    plt.savefig(output_dir / f"residuales_{best_name}.png", dpi=150)
    plt.close()

    # Metrics comparison bar plot
    results_df.set_index("model")[["RMSE", "MAE"]].plot.bar(rot=0, figsize=(7,4))
    plt.title("Comparativa de métricas")
    plt.tight_layout()
    plt.savefig(output_dir / "metrics_comparison.png", dpi=150)
    plt.close()

    # If RandomForest, extract feature importances (need to get feature names after preprocessing)
    if "RandomForest" in best_estimators:
        rf_pipeline = best_estimators["RandomForest"]
        # Extract the random forest model and preprocessor
        pre = rf_pipeline.named_steps["pre"]
        rf = rf_pipeline.named_steps["model"]
        # Build feature names
        feature_names = []
        # numeric names are num_cols but they were defined outside function; reconstruct from transformer
        # Get numeric and categorical transformers from ColumnTransformer
        for name, trans, cols in pre.transformers_:
            if name == "num":
                feature_names.extend(cols)
            elif name == "cat":
                # OneHotEncoder categories
                ohe = trans.named_steps["onehot"]
                cats = ohe.categories_
                # prepend column name to category value for clarity
                for col, cat_list in zip(cols, cats):
                    for cat in cat_list:
                        feature_names.append(f"{col}__{cat}")
        # Save importances
        importances = pd.DataFrame({
            "feature": feature_names,
            "importance": rf.feature_importances_
        }).sort_values("importance", ascending=False)
        importances.to_csv(output_dir / "feature_importances_rf.csv", index=False)

    print("All outputs saved in folder:", output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train KNN, RF, SVR on California Housing dataset")
    parser.add_argument("--data", type=str, default="california_housing.csv", help="Path to california_housing.csv")
    args = parser.parse_args()
    main(args)

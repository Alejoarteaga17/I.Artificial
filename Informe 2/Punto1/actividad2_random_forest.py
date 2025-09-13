# actividad2_random_forest.py
# Actividad 2 - Random Forest con Pipeline

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import joblib

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ================================
# 1. CARGA DE DATOS
# ================================
print("Cargando datos...")
df = pd.read_csv("fetch_california_housing.csv")
print("Columnas:", list(df.columns))
print("Tamaño:", df.shape)

target_col = "MedHouseVal" if "MedHouseVal" in df.columns else df.columns[-1]
X = df.drop(columns=[target_col])
y = df[target_col]

# ================================
# 2. DIVISIÓN TRAIN/TEST
# ================================
print("\nSeparando datos...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ================================
# 3. PIPELINE RANDOM FOREST
# ================================
print("\nEntrenando modelo Random Forest con Pipeline...")

pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler()),
    ('model', RandomForestRegressor(
        n_estimators=100,
        max_depth=15,
        random_state=42,
        n_jobs=-1
    ))
])

pipeline.fit(X_train, y_train)

# ================================
# 4. EVALUACIÓN
# ================================
print("\nEvaluando modelo...")
y_pred = pipeline.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"MAE  = {mae:.3f}")
print(f"MSE  = {mse:.3f}")
print(f"RMSE = {rmse:.3f}")
print(f"R²   = {r2:.4f}")

# ================================
# 5. GUARDADO DE RESULTADOS
# ================================
os.makedirs("resultados", exist_ok=True)

joblib.dump(pipeline, "resultados/random_forest_pipeline.pkl")

pd.DataFrame({"metric": ["MAE", "MSE", "RMSE", "R2"],
              "value": [mae, mse, rmse, r2]}).to_csv("resultados/rf_metrics.csv", index=False)

pd.DataFrame({"y_true": y_test, "y_pred": y_pred}).to_csv("resultados/rf_results.csv", index=False)

# Extra: obtener importancia de características del modelo interno
rf_model = pipeline.named_steps['model']
feat_imp = pd.Series(rf_model.feature_importances_, index=X.columns).sort_values(ascending=False)
feat_imp.to_frame("importance").to_csv("resultados/rf_feature_importances.csv")

print("\n💾 Archivos guardados en carpeta 'resultados/'")

# ================================
# 6. VISUALIZACIONES
# ================================
plt.figure(figsize=(10, 5))
feat_imp.plot(kind="bar")
plt.title("Importancia de características")
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 6))
plt.scatter(y_test, y_pred, alpha=0.3)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r')
plt.xlabel("Valor real")
plt.ylabel("Predicción")
plt.title("Real vs Predicho")
plt.tight_layout()
plt.show()

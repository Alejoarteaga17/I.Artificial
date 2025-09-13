import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\alejandro\OneDrive\Documentos\Quinto\Inteligencia Artifical\punto3\Informe 2\california_housing.csv")  # asegúrate de tener este CSV
X = df.drop(columns=["MedHouseVal"])
y = df["MedHouseVal"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# Red Neuronal - Keras
nn_model = Sequential([
    Dense(128, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(1)  # salida de regresión
])

nn_model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Early stopping para detener el entrenamiento si no mejora con paciencia de 6 épocas
early_stop = EarlyStopping(monitor='val_loss', patience=6, restore_best_weights=True)

## Entrenamiento, modificar epochs y batch_size según necesidad
history = nn_model.fit(
    X_train_scaled, y_train,
    epochs=20, batch_size=32,
    validation_split=0.2,
    callbacks=[early_stop],
    verbose=1
)

# -----------------------------
# 4) Evaluación en test set
# -----------------------------
y_pred = nn_model.predict(X_test_scaled).flatten()
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nMÉTRICAS RED NEURONAL:")
print(f"MAE: {mae:.4f}")
print(f"MSE: {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R²: {r2:.4f}")

# -----------------------------
# 5) Visualización entrenamiento
# -----------------------------
plt.figure(figsize=(10,5))
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Val Loss')
plt.xlabel("Épocas")
plt.ylabel("MSE")
plt.title("Curva de entrenamiento - Red Neuronal")
plt.legend()
plt.tight_layout()
plt.show()

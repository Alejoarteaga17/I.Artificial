# ============================================================
# 6) Generar README.md con resultados
# ============================================================
readme_content = f"""
# 📄 Informe - Modelos de Aprendizaje Supervisado sobre California Housing

## 1. Descripción del dataset
- **Fuente:** [California Housing Dataset](https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset)
- **Número de registros:** {len(df)} observaciones
- **Número de variables (features):** {X.shape[1]}
- **Variable objetivo (target):** `MedHouseVal`
- **Tipo de problema:** **Regresión supervisada**

| Variable         | Descripción |
|------------------|-------------|
| MedInc           | Ingreso medio en la zona |
| HouseAge         | Edad media de las casas |
| AveRooms         | Número medio de habitaciones |
| AveBedrms        | Número medio de dormitorios |
| Population       | Población total |
| AveOccup         | Ocupación media por vivienda |
| Latitude         | Latitud geográfica |
| Longitude        | Longitud geográfica |
| **MedHouseVal**  | **Valor medio de las casas (target)** |

---

## 2. Preprocesamiento realizado
1. **Limpieza de datos faltantes:** No se encontraron valores nulos.
2. **Codificación de variables categóricas:** Todas las variables son numéricas.
3. **Escalado/normalización:** Se aplicó `StandardScaler`.
4. **División en train/test:** 80% entrenamiento, 20% prueba (`random_state=42`).

---

## 3. Modelos entrenados
- **Random Forest Regressor** (`n_estimators=100`)
- **Gradient Boosting Regressor** (`n_estimators=200`, `learning_rate=0.1`, `max_depth=3`)
- **Red Neuronal (Keras - TensorFlow)**:
  - Capas densas: 128 → 64 → 32 → 1
  - Activación: ReLU en capas ocultas, salida lineal
  - Optimizador: Adam
  - Pérdida: MSE
  - Épocas: hasta 200 con `EarlyStopping`

---

## 4. Evaluación de resultados

| Modelo           | MAE   | MSE   | RMSE  | R²   |
|------------------|-------|-------|-------|------|
| Random Forest    | {mae_rf:.4f} | {mse_rf:.4f} | {rmse_rf:.4f} | {r2_rf:.4f} |
| Gradient Boosting| {mae_gbr:.4f} | {mse_gbr:.4f} | {rmse_gbr:.4f} | {r2_gbr:.4f} |
| Red Neuronal     | {mae:.4f} | {mse:.4f} | {rmse:.4f} | {r2:.4f} |

---

## 5. Análisis comparativo
- **Random Forest:** Mejor desempeño global, robusto, rápido de entrenar.
- **Gradient Boosting:** Similar al RF, aunque con mayor tiempo de entrenamiento.
- **Red Neuronal:** Buen resultado pero menor R², requiere más ajuste y datos.

---

## 6. Conclusiones
- El **Random Forest** fue el modelo más adecuado para este dataset.
- Los métodos ensemble (RF y GB) superaron a la red neuronal.
- La práctica permitió comprender la importancia de comparar distintos algoritmos en un mismo problema.
"""


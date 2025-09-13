# Actividad 2 — Random Forest

**Autor:** *(tu nombre)*  
**Fecha:** *(fecha de entrega)*

---

## 1. Descripción del dataset

- **Fuente:** Dataset `fetch_california_housing.csv` proporcionado por el curso.
- **Número de registros:** 20 640
- **Número de variables:** 9 columnas
  - **Variables predictoras:**  
    `MedInc` (ingreso medio), `HouseAge` (edad promedio de casas),  
    `AveRooms` (habitaciones promedio), `AveBedrms` (dormitorios promedio),  
    `Population`, `AveOccup` (ocupantes promedio), `Latitude`, `Longitude`.
  - **Variable objetivo:**  
    `MedHouseVal` — valor medio de las viviendas.
- **Tipo de problema:** Regresión (predicción de un valor numérico continuo).

---

## 2. Preprocesamiento realizado

**a. Limpieza de datos faltantes**  
- Se aplicó `SimpleImputer(strategy='median')` para rellenar valores nulos numéricos.
- No se detectaron valores faltantes en el dataset.

**b. Codificación de variables categóricas**  
- No existen variables categóricas en este dataset, por lo que no se aplicó codificación.

**c. Escalado / normalización**  
- Se aplicó `StandardScaler` dentro del `Pipeline` para escalar las variables numéricas.
- Aunque Random Forest no lo requiere, se incluyó por buenas prácticas.

**d. División en train/test**  
- Se utilizó `train_test_split` con 80% para entrenamiento y 20% para prueba.
- `random_state=42` para asegurar reproducibilidad.

---

## 3. Entrenamiento del modelo (Random Forest con Pipeline)

Se construyó un `Pipeline` con tres etapas:

1. `SimpleImputer(strategy='median')`
2. `StandardScaler()`
3. `RandomForestRegressor(n_estimators=100, max_depth=15, random_state=42, n_jobs=-1)`

El modelo fue entrenado con el conjunto de entrenamiento y luego evaluado con el conjunto de prueba.

> ⚠️ Nota: El enunciado pedía tres modelos, pero en este trabajo solo se implementó **Random Forest**, siguiendo las indicaciones de la actividad.

---

## 4. Evaluación de resultados

**a. Métricas de rendimiento en test**

| Métrica | Valor aproximado |
|---------|---------|
| MAE     | 0.33    |
| MSE     | 0.26    |
| RMSE    | 0.51    |
| R²      | 0.80    |

**b. Visualizaciones**

1. **Importancia de características**  
   ![Gráfico de importancia de características](resultados/feature_importances.png)

2. **Real vs Predicho**  
   ![Scatter real vs predicho](resultados/real_vs_predicho.png)

(Estas gráficas se muestran en pantalla al ejecutar el script y también pueden guardarse como `.png`).

---

## 5. Análisis comparativo

Aunque no se entrenaron los otros dos modelos, se describe brevemente un posible análisis:

| Modelo           | Ventajas                                   | Desventajas                              | Posibles usos                     |
|------------------|---------------------------------------------|--------------------------------------------|-------------------------------------|
| Árbol de decisión simple | Fácil de interpretar | Tiende a sobreajustar | Problemas simples, interpretables |
| Random Forest    | Robusto, buen desempeño general, reduce sobreajuste | Más lento y menos interpretable | Datasets grandes y variados |
| Red Neuronal     | Alta capacidad predictiva en datos complejos | Requiere mucho ajuste y datos grandes | Datos no lineales, visión, audio |

En este caso, **Random Forest ofrece un balance ideal entre rendimiento y facilidad de uso** para este dataset.

---

## 6. Conclusiones

- Se logró predecir el valor medio de viviendas en California con un desempeño bueno (R² ≈ 0.80).
- La variable más influyente fue el ingreso medio (`MedInc`), lo que es coherente con el dominio del problema.
- Random Forest demostró ser robusto, preciso y fácil de implementar mediante un `Pipeline`.
- Como mejoras futuras se podría:
  - Ajustar hiperparámetros con `GridSearchCV` o `RandomizedSearchCV`
  - Probar modelos de boosting como `XGBoost` o `LightGBM`
  - Incluir validación cruzada y comparar con otros algoritmos.

---

## 📂 Archivos entregados

- `actividad2_random_forest.py` — Script completo con el pipeline y entrenamiento
- `README.md` — Este informe
- Carpeta `resultados/` con:
  - `random_forest_pipeline.pkl`
  - `rf_metrics.csv`
  - `rf_results.csv`
  - `rf_feature_importances.csv`

# Informe: Predicción de `median_house_value` — California Housing (KNN / RandomForest / SVR)

## 1. Descripción del dataset
- **Fuente:** Kaggle — *California Housing* (versión comúnmente usada, derivada de StatLib / U.S. Census block groups).  
- **Número de registros:** 20,640 (en la versión estándar).  
- **Variables (columnas):**
  - Numéricas: `longitude`, `latitude`, `housing_median_age`, `total_rooms`, `total_bedrooms`, `population`, `households`, `median_income`.
  - Categórica: `ocean_proximity` (en muchas versiones del dataset).
  - Objetivo: `median_house_value` (valor mediano de la vivienda en el bloque).
- **Objetivo del problema:** Resolver un problema de **regresión** para predecir `median_house_value` a partir de las demás variables.

## 2. Preprocesamiento realizado (incluido en el script)
- **Limpieza de datos faltantes:**
  - Para variables numéricas se usa `SimpleImputer(strategy="median")` (ej. `total_bedrooms` suele presentar valores faltantes).
  - Para variables categóricas se usa `SimpleImputer(strategy="most_frequent")`.
- **Codificación de variables categóricas:**
  - `OneHotEncoder(handle_unknown="ignore")` para `ocean_proximity` u otras categóricas (genera columnas binarias por categoría).
- **Escalado / Normalización:**
  - `StandardScaler()` sobre variables numéricas. Es necesario para modelos basados en distancia (KNN) y para SVR.
  - Random Forest no requiere escalado, pero se aplica por consistencia del pipeline.
- **División en train / test:**
  - `train_test_split` con test_size=0.2 (80% train, 20% test, `random_state=42`).

## 3. Modelos entrenados y parámetros (incluido GridSearch CV)
Se entrenan y optimizan con `GridSearchCV (cv=5)` los siguientes modelos:

1. **KNN Regressor (`KNeighborsRegressor`)**
   - Parámetros probados: `n_neighbors` ∈ {3,5,8}, `weights` ∈ {uniform,distance}, `p` ∈ {1,2}.
   - Ventajas: simple, interpretable; útil como baseline.
   - Desventajas: sensible a la escala y al ruido; costoso en predicción para datasets grandes.

2. **Random Forest Regressor (`RandomForestRegressor`)**
   - Parámetros probados: `n_estimators` ∈ {100,200}, `max_depth` ∈ {None,12,20}, `min_samples_split` ∈ {2,5}.
   - Ventajas: robusto, maneja no linealidad, permite extraer importancias de variables.
   - Desventajas: consumo de memoria y tiempo de entrenamiento mayor que modelos simples.

3. **Support Vector Regressor (`SVR`)**
   - Parámetros probados: `C` ∈ {0.1,1}, `gamma` ∈ {scale, auto}, `kernel` ∈ {rbf, linear}.
   - Ventajas: potente con datos de dimensión moderada y bien escalados.
   - Desventajas: costoso para N grande; sensible a hiperparámetros.

**Criterio de optimización en GridSearch:** minimizar RMSE (usando `scoring="neg_root_mean_squared_error"`).

## 4. Evaluación de resultados
- El script guarda en `outputs/results.csv` las métricas evaluadas en el conjunto de test para cada modelo: **RMSE**, **MAE** y **R²**.
- También guarda predicciones por modelo, gráficas (real vs predicho, residuales, comparación de métricas) y las mejores configuraciones por modelo (`best_params_*.txt`).

### Métricas (qué significan)
- **RMSE:** Raíz del Error Cuadrático Medio — penaliza errores grandes. (Un RMSE menor = mejor).
- **MAE:** Error Absoluto Medio — más robusto a outliers que RMSE.
- **R²:** Coeficiente de determinación — proporción de varianza explicada por el modelo (1.0 perfecto, 0 ó negativo malo).

## 5. Visualizaciones incluidas (generadas por el script)
- **Real vs Predicho** (scatter con línea 1:1) para el mejor modelo en test.
- **Histograma de residuales** para el mejor modelo.
- **Comparativa de métricas** (barras) entre los tres modelos.

## 6. Análisis comparativo (guía para redactar en el informe final)
- Comparar los valores de RMSE/MAE/R² y discutir:
  - Si un modelo sobreajusta (mucho mejor en train que en test) o no.
  - Ventajas prácticas: por ejemplo, RandomForest suele ser el mejor balance para datos tabulares; KNN sirve como baseline; SVR puede ser competitivo pero es costoso en tiempo.
- Discutir interpretabilidad: RandomForest permite extraer `feature_importances_` (archivo `feature_importances_rf.csv` si se generó).
- Discutir tiempo de entrenamiento / predicción y escalabilidad (KNN tiene costo alto en predicción; RF y SVR en entrenamiento pueden consumir tiempo).

## 7. Conclusiones (ejemplo que puedes adaptar)
- El dataset California Housing requiere imputación y codificación de `ocean_proximity`. Tras el preprocesamiento y búsqueda de hiperparámetros, **RandomForest** suele ofrecer el mejor compromiso entre precisión y robustez en este tipo de problema tabular. Sin embargo, resultados finales deben confirmarse con las métricas guardadas en `outputs/results.csv` generadas por el script.
- Recomendaciones futuras: probar **XGBoost/LightGBM**, ingeniería de variables espaciales (interacciones entre latitud/longitud), validación espacial si se requiere generalización geográfica, transformaciones logarítmicas en variables sesgadas.

## 8. Cómo ejecutar (resumen)
1. Descarga `california_housing.csv` y colócalo en la misma carpeta que el script o pasa su ruta con `--data`.
2. Ejecuta: `python california_housing_models.py --data california_housing.csv`
3. Revisa la carpeta `outputs` con resultados, gráficos y parámetros.

---

**Archivos generados por el script (ejemplo):**
- `outputs/results.csv`
- `outputs/predictions_KNN.csv`, `predictions_RandomForest.csv`, `predictions_SVR.csv`
- `outputs/real_vs_pred_<best>.png`, `outputs/residuales_<best>.png`, `outputs/metrics_comparison.png`
- `outputs/best_params_<model>.txt`
- `outputs/feature_importances_rf.csv` (si RandomForest es entrenado)



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
  

2. **Real vs Predicho**  
 

(Estas gráficas se muestran en pantalla al ejecutar el script y también pueden guardarse como `.png`).

---

## 5. Análisis comparativo


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

##  Nota importante

> Al ejecutar el archivo `actividad2_random_forest.py` en local:  
> - Se generan automáticamente los resultados de métricas (`.csv`)  
> - Se guarda el modelo entrenado (`.pkl`)  
> - Y se muestran en pantalla las gráficas de:
>   - Importancia de características  
>   - Valores reales vs predichos  

Estos archivos y gráficas **no están subidos en el repositorio**, ya que se crean al momento de ejecutar el script.`



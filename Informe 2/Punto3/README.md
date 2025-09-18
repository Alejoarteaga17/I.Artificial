## 1. Descripción del dataset

- **Fuente:** Dataset `fetch_california_housing.csv`, también disponible en Kaggle.
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
- En este dataset no se encontraron valores faltantes.

**b. Codificación de variables categóricas**  
- El dataset no contiene variables categóricas, por lo que no se requirió codificación.

**c. Escalado / normalización**  
- Se utilizó `StandardScaler` para normalizar todas las variables numéricas, ya que **KNN es muy sensible a la escala** de los datos.

**d. División en train/test**  
- Se usó `train_test_split` con 80% de los datos para entrenamiento y 20% para prueba.
- Se fijó `random_state=42` para garantizar reproducibilidad.

---

## 3. Modelo

- **K-Nearest Neighbors (KNN Regressor)**:
  - Número de vecinos: `k=5` (valor inicial, aunque se puede optimizar con GridSearchCV).
  - Métrica de distancia: Euclidiana (por defecto en scikit-learn).
  - Ponderación: Uniforme (todos los vecinos tienen el mismo peso).
  - Implementado con `KNeighborsRegressor` de scikit-learn.

---

## 4. Evaluación de resultados

| Modelo  | MAE    | MSE    | RMSE   | R²    |
|---------|--------|--------|--------|-------|
| KNN     | ~0.48  | ~0.42  | ~0.65  | ~0.68 |

*(valores aproximados, varían según el número de vecinos y preprocesamiento aplicado)*

---

## 5. Análisis

- **KNN:**  
  - Resultados aceptables, aunque con menor R² que modelos más complejos como Random Forest o Redes Neuronales.  
  - Ventajas: Fácil de implementar, no requiere entrenamiento complejo, funciona bien en datasets pequeños.  
  - Desventajas: Lento en datasets grandes, depende mucho de la escala de los datos y de la elección de *k*.  
  - En este dataset, el modelo mostró un desempeño correcto, pero inferior a modelos más avanzados que capturan mejor la relación no lineal entre variables.

---

## 6. Conclusiones

- El algoritmo **KNN** es útil como modelo base para problemas de regresión, pero no es el más eficiente en datasets grandes como *California Housing*.  
- Aunque logra un R² aceptable (~0.68), queda por debajo del desempeño obtenido con **Árboles de Decisión, Random Forest o Redes Neuronales**.  
- Aumentar el número de vecinos o usar ponderaciones por distancia puede mejorar ligeramente los resultados, pero a costa de mayor tiempo de cómputo.  
- En conclusión, **KNN no es la técnica más adecuada para este dataset en particular**, pero es valiosa para entender los fundamentos de regresión basada en distancias y sirve como baseline comparativo.

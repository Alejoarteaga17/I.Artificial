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

## 3. Modelo
- **Red Neuronal (Keras - TensorFlow)**:
  - Capas densas: 128 → 64 → 32 → 1
  - Activación: ReLU en capas ocultas, salida lineal
  - Optimizador: Adam como en clase
  - Pérdida: MSE
  - Épocas: Usamos hasta 20 con `EarlyStopping` para evitar tiempos muy largos de ejecucion pero vimos que seguia disminuyendo (inlcuso al pasar las 20 epocas) la perdida por lo que asumo que si aumentamos las épocas a numeros más grandes podemos obtener un mejor resultado de entrenamiento; y con ayuda de un early stop con una paciencia baja evitariamos que se sigan realizando épocas sin mejoras

## 4. Evaluación de resultados

| Modelo           | MAE   | MSE   | RMSE  | R²   |
|------------------|-------|-------|-------|------|
| Red Neuronal     | 0.3970 | 0.2959 | 0.5440 | 0.7742 |


## 5. Análisis
- **Red Neuronal:** Buen resultado pero menor R², requiere más ajuste, tiene mejores resultados en grandes cantidades de epocas y es mas eficiente, y mejores resultados esperados si tiene una base de datos mas amplia.

- 
## 6. Conclusiones
- Como lo estaba mencionando anteriormente, este algorimo de RN tiene buenos resultados pero son menores a los otros dos que aplicamos, el los casos de ejecucion vemos buenos resultados pero analizamos que si aumentamos las epocas (con esta cantidad de datos) podemos obtener mejores resultados aun, además si ajustamos el optimizador a los valores usados en clase (0.01) vemos un mejor entrenamiento y una linea de ajuste mucho mas cercana a lo esperado, todo esto, teniendo peores resultados a los otros algoritmos ejecutados. 

Asumo que si hacemos otros cambios en el algoritmo relacionados al optimizador (inlcuyendo cambio de tipo), cambio de epocas y las condiciones aplicadas a cada uno podriamos llegar a resultados incluso mas cercanos a lo esperados, pero a pesar de no ser el mejor, es un buen mecanismo de regresion



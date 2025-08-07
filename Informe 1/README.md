# README Informe 1
    Solucion a las preguntas planteadas en el documento del informe 1 para cada uno de los ejercicios:
    
## Autores
- Alejandra Ortiz
- Alejandro Arteaga
- Camila Velez

# Ejercicio 1 - Algoritmo A* para encontrar ruta óptima a Bucarest

## Análisis del problema

Este problema consiste en encontrar la **ruta más corta desde Arad hasta Bucarest**, utilizando el algoritmo A* (A-Star), el cual considera tanto el costo real del camino recorrido como una estimación heurística del costo restante hasta el objetivo.

- **Estado inicial:** Arad
- **Estado objetivo:** Bucarest
- **Acciones:** Transiciones entre ciudades conectadas.
- **Costos:** Las distancias entre ciudades (costos uniformes reales).
- **Heurística:** Estimación en línea recta hacia Bucarest.

## ¿Cómo se aplica A*?

El algoritmo A* busca el camino más corto utilizando la función de evaluación:

```
f(n) = g(n) + h(n)
```
- `g(n)`: Costo del camino desde el inicio hasta el nodo `n`.
- `h(n)`: Estimación heurística del costo desde `n` hasta el objetivo (en este caso, distancias en línea recta a Bucarest).

El algoritmo mantiene una cola de prioridad (heap) ordenada por `f(n)` y expande siempre el nodo con el menor valor de esta función.

## ¿Por qué se considera óptima la ruta?

La ruta encontrada es óptima **porque A\*** con una heurística **admisible** y **consistente** (como lo es la distancia en línea recta a Bucarest) **garantiza encontrar la solución de costo mínimo**.

## Resultado del código

Ruta óptima encontrada:

```
['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']
```

Esta es la ruta más eficiente en términos de costo total (distancia).

# Ejercicio 2 - Problema del Laberinto


## 1. ¿Cómo cambia el comportamiento del algoritmo si cambiamos la función de costo?

 R/= Si usamos un costo mayor para ciertas celdas, el robot evitará esas zonas si encuentra caminos más baratos, aunque sean más largos.
Si la función de costo ya no representa bien el costo real del camino (asignar valores negativos o irreales), A* puede dejar de encontrar el camino óptimo, o incluso no encontrar ninguno.

## 2.  ¿Qué sucede si hay múltiples salidas en el laberinto? ¿Cómo podrías modificar el algoritmo para manejar esto? Plantea una propuesta.

 R/= Si hay múltiples salidas, por ejemplo, varias ‘E’,en el laberinto y el algoritmo sigue buscando una posición específica, sólo encontrará la que coincida exactamente con la coordenada end.

Propuesta para solucionarlo:
- Paso 1: Buscar todas las coordenadas que contienen ‘E’ y guardarlas en una lista:

goals = [(i, j) for i in range(len(maze)) for j in range(len(maze[0])) if maze[i][j] == 'E']

- Paso 2: Durante la búsqueda, verificar si el nodo actual está en esa lista de salidas:

if node.position in goals:
    return reconstruct_path(node)

## 3. Modifica el laberinto por uno más grande y con otro tipo de obstáculo además de paredes. ¿Qué limitación encuentras en el algoritmo? 


 R/= Al aumentar el tamaño del laberinto y los tipos de obstáculos, pueden surgir varias limitaciones:
 
**Consumo de memoria y tiempo:**
- A* puede explorar muchos nodos si el laberinto es grande.
- Puede volverse muy lento o incluso inviable si el espacio de búsqueda es enorme.

**Obstáculos no manejados:**
- Si hay nuevos tipos de obstáculos (como trampas, zonas con alto costo, o caminos temporales), el algoritmo necesitaría saber cómo tratar cada tipo, es decir, una función de costo personalizada.

**El algoritmo no adapta estrategias inteligentes:**
- No aprende ni adapta su comportamiento. No sabrá, por ejemplo, evitar un área que siempre resulta en caminos sin salida a menos que lo "descubra" mediante la exploración completa.


# Ejercicio 3 – Navegación en una Red de Metro (BFS e IDS)
## Análisis del Problema

- **Estado Inicial:** La estación donde comienza el pasajero (por ejemplo, 'A').
- **Estado Objetivo:** La estación de destino (por ejemplo, 'J').
- **Acciones:** Desde cada estación, el pasajero puede moverse a cualquier estación conectada directamente.
- **Espacio de Estados:** Todas las posibles combinaciones de estaciones conectadas por las rutas.
- **Modelo de Transición:** Cada movimiento representa una transición de un nodo a otro adyacente.

## Diseño del Grafo

Se construyó una representación del mapa de metro como un diccionario donde las claves son las estaciones y los valores las estaciones adyacentes.

## Algoritmos Implementados

### Breadth-First Search (BFS)
- Explora los nodos por niveles.
- Usa una cola FIFO.
- Encuentra la ruta más corta en términos de número de pasos.
- Es eficiente para encontrar caminos cortos en grafos con ramas uniformes.

### Iterative Deepening Search (IDS)
- Combinación de Búsqueda en Profundidad y BFS.
- Limita la profundidad en cada iteración y reinicia.
- Utiliza menos memoria que BFS.
- Garantiza la ruta más corta al igual que BFS.

## Resultados: A → J

### BFS
- Ruta: A → C → F → J
- Tiempo de ejecución: Rápido
- Memoria utilizada: Mayor que IDS

### IDS
- Ruta: A → C → F → J
- Tiempo de ejecución: Rapido
- Memoria utilizada: Menor que BFS

## Comparación

| Algoritmo | Tiempo (s) | Memoria (KB) | Ruta Encontrada |
|-----------|------------|--------------|------------------|
| BFS       | Bajo       | Alta         | ['A', 'C', 'F', 'J'] |
| IDS       | Medio-Bajo | Baja         | ['A', 'C', 'F', 'J'] |

## Conclusión

Ambos algoritmos encuentran la misma ruta óptima. BFS es más rápido en este problema, pero consume más memoria. IDS es más conservador en memoria, pero tarda un poco más debido a su naturaleza repetitiva. Se recomienda BFS cuando hay recursos suficientes y se requiere velocidad.
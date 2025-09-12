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
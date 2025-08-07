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
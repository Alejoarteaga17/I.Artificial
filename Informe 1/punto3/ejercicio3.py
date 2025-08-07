from collections import deque
import time
import tracemalloc

# Definición de la clase de Nodo
class Node:
    def __init__(self, estado, padre=None, profundidad=0):
        self.estado = estado
        self.padre = padre
        self.profundidad = profundidad

    def path(self):
        node, p = self, []
        while node:
            p.append(node.estado)
            node = node.padre
        return list(reversed(p))
#Definicion de la clase Problem
class Problem:
    def __init__(self, inicial, objetivo, graph):
        self.inicial = inicial
        self.objetivo = objetivo
        self.graph = graph

    def actions(self, estado):
        return self.graph.get(estado, [])

    def result(self, estado, action):
        return action

    def is_objetivo(self, estado):
        return estado == self.objetivo
# Definición del grafo de estaciones de metro
metro_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'H', 'I'],
    'F': ['C', 'J'],
    'G': ['D'],
    'H': ['E'],
    'I': ['E', 'J'],
    'J': ['F', 'I']
}

# Algoritmo BFS (Breadth-First Search)
def bfs(problem):
    frontier = deque([Node(problem.inicial)])
    explored = set()

    while frontier:
        node = frontier.popleft()
        if problem.is_objetivo(node.estado):
            return node
        explored.add(node.estado)
        for action in problem.actions(node.estado):
            hijo_estado = problem.result(node.estado, action)
            if hijo_estado not in explored and all(n.estado != hijo_estado for n in frontier):
                frontier.append(Node(hijo_estado, node))
    return None
# Algoritmo IDS (Iterative Deepening Search)
def dls(node, problem, limit):
    if problem.is_objetivo(node.estado):
        return node
    elif limit == 0:
        return None
    else:
        for action in problem.actions(node.estado):
            hijo_estado = problem.result(node.estado, action)
            hijo = Node(hijo_estado, node, node.profundidad + 1)
            result = dls(hijo, problem, limit - 1)
            if result:
                return result
    return None

def ids(problem):
    profundidad = 0
    while True:
        result = dls(Node(problem.inicial), problem, profundidad)
        if result:
            return result
        profundidad += 1

# Comparación
def mediciones(func, problem):
    tracemalloc.start()
    start_time = time.time()
    result = func(problem)
    end_time = time.time()
    memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return result, end_time - start_time, memory

problem = Problem('A', 'J', metro_graph)
#problem = Problem('J', 'G', metro_graph) Linea de prueba

bfs_result, bfs_time, bfs_memory = mediciones(bfs, problem)
ids_result, ids_time, ids_memory = mediciones(ids, problem)

print("\nCamino usado en BFS:", bfs_result.path() if bfs_result else "No se encontró un camino")
print("Camino usado en IDS:", ids_result.path() if ids_result else "No se encontró un camino")
print("---")
print(f"Tiempo ejecutando BFS: {bfs_time:.6f}s, Uso de memoria: {bfs_memory[1] / 1024:.2f} KB")
print(f"Tiempo ejecutando IDS: {ids_time:.6f}s, Uso de memoria: {ids_memory[1] / 1024:.2f} KB", end="\n")
import heapq  # El módulo heapq implementa colas de prioridad (heaps)

class Node:
    def __init__(self, position, parent=None, path_cost=0, action=None):
        self.position = position
        self.parent = parent
        self.path_cost = path_cost
        self.action = action

    def __lt__(self, other):
        return self.path_cost < other.path_cost

class Problem:
    def __init__(self, maze, start, goal):
        self.maze = maze
        self.start = start
        self.goal = goal
        self.actions = {
            (-1, 0): "Up",
            (1, 0): "Down",
            (0, -1): "Left",
            (0, 1): "Right"
        }

    def is_valid_position(self, position):
        i, j = position
        return 0 <= i < len(self.maze) and 0 <= j < len(self.maze[0]) and self.maze[i][j] != "#"

def manhattan_distance(pos, goal):
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

def get_neighbors(pos, problem):
    neighbors = []
    for move, action in problem.actions.items():
        neighbor = (pos[0] + move[0], pos[1] + move[1])
        if problem.is_valid_position(neighbor):
            neighbors.append((neighbor, action))
    return neighbors

def reconstruct_path(node):
    path = []
    actions = []
    while node.parent is not None:
        path.append(node.position)
        actions.append(node.action)
        node = node.parent
    path.append(node.position)
    path.reverse()
    actions.reverse()
    return path, actions

def find_exit(maze):
    start = (1, 1)
    end = (1, 6)
    problem = Problem(maze, start, end)

    start_node = Node(start, path_cost=0)
    frontier = [(manhattan_distance(start, end), start_node)]
    heapq.heapify(frontier)
    reached = {start: start_node}

    while frontier:
        _, node = heapq.heappop(frontier)
        if node.position == end:
            return reconstruct_path(node)

        for neighbor, action in get_neighbors(node.position, problem):
            new_cost = node.path_cost + 1
            if neighbor not in reached or new_cost < reached[neighbor].path_cost:
                reached[neighbor] = Node(neighbor, parent=node, path_cost=new_cost, action=action)
                heapq.heappush(frontier, (new_cost + manhattan_distance(neighbor, end), reached[neighbor]))

    return None, None  # No se encontró salida

# Laberinto
maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "S", "#", " ", "#", " ", "E", "#"],
    ["#", " ", " ", " ", "#", " ", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#"]
]

# Ejecutar
path, actions = find_exit(maze)
print("\nPath to exit:", path)
print("Actions taken:", actions, end="")

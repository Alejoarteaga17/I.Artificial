import heapq

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __lt__(self, other):
        return self.path_cost < other.path_cost

def expand(problem, node):
    children = []
    for action in problem.actions(node.state):
        child_state = problem.result(node.state, action)
        cost = node.path_cost + problem.action_cost(node.state, action, child_state)
        child_node = Node(child_state, node, action, cost)
        children.append(child_node)
    return children

class Problem:
    def __init__(self, initial, goal, actions, result, action_cost, is_goal):
        self.initial = initial
        self.goal = goal
        self.actions = actions
        self.result = result
        self.action_cost = action_cost
        self.is_goal = is_goal

def best_first_search(problem, f):
    node = Node(state=problem.initial)
    frontier = [(f(node), node)]
    heapq.heapify(frontier)
    reached = {problem.initial: node}

    while frontier:
        _, node = heapq.heappop(frontier)
        if problem.is_goal(node.state):
            return node

        for child in expand(problem, node):
            s = child.state
            if s not in reached or child.path_cost < reached[s].path_cost:
                reached[s] = child
                heapq.heappush(frontier, (f(child), child))

    return None

def result(state, action):
    return action

def action_cost(state, action, result):
    return action_costs.get((state, action), float('inf'))

def is_goal(state):
    return state == goal

def f(node):
    return node.path_cost + heuristic.get(node.state, float('inf'))

initial = 'Arad'
goal = 'Bucharest'

actions = {
    'Arad': ['Sibiu', 'Timisoara', 'Zerind'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti']
}

action_costs = {
    ('Arad', 'Zerind'): 75,
    ('Zerind', 'Arad'): 75,
    ('Zerind', 'Oradea'): 71,
    ('Oradea', 'Zerind'): 71,
    ('Oradea', 'Sibiu'): 151,
    ('Sibiu', 'Oradea'): 151,
    ('Arad', 'Sibiu'): 140,
    ('Sibiu', 'Arad'): 140,
    ('Arad', 'Timisoara'): 118,
    ('Timisoara', 'Arad'): 118,
    ('Timisoara', 'Lugoj'): 111,
    ('Lugoj', 'Timisoara'): 111,
    ('Lugoj', 'Mehadia'): 70,
    ('Mehadia', 'Lugoj'): 70,
    ('Mehadia', 'Drobeta'): 75,
    ('Drobeta', 'Mehadia'): 75,
    ('Drobeta', 'Craiova'): 120,
    ('Craiova', 'Drobeta'): 120,
    ('Craiova', 'Rimnicu Vilcea'): 146,
    ('Rimnicu Vilcea', 'Craiova'): 146,
    ('Sibiu', 'Fagaras'): 99,
    ('Fagaras', 'Sibiu'): 99,
    ('Sibiu', 'Rimnicu Vilcea'): 80,
    ('Rimnicu Vilcea', 'Sibiu'): 80,
    ('Rimnicu Vilcea', 'Pitesti'): 97,
    ('Pitesti', 'Rimnicu Vilcea'): 97,
    ('Craiova', 'Pitesti'): 138,
    ('Pitesti', 'Craiova'): 138,
    ('Fagaras', 'Bucharest'): 211,
    ('Bucharest', 'Fagaras'): 211,
    ('Pitesti', 'Bucharest'): 101,
    ('Bucharest', 'Pitesti'): 101
}

heuristic = {
    'Arad': 366,
    'Zerind': 374,
    'Oradea': 380,
    'Sibiu': 253,
    'Timisoara': 329,
    'Lugoj': 244,
    'Mehadia': 241,
    'Drobeta': 242,
    'Craiova': 160,
    'Rimnicu Vilcea': 193,
    'Fagaras': 176,
    'Pitesti': 100,
    'Bucharest': 0
}

problem = Problem(initial, goal, lambda s: actions.get(s, []), result, action_cost, is_goal)
solution = best_first_search(problem, f)

if solution:
    path = []
    while solution:
        path.append(solution.state)
        solution = solution.parent
    path.reverse()
    print("Solution path:", path)
else:
    print("No solution found")
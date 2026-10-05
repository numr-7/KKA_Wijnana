from collections import deque
from queue import PriorityQueue

romania_graph = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
    'Dobreta': [('Mehadia', 75), ('Craiova', 120)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Craiova': [('Dobreta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

def bfs(graph, start, goal):
    queue = deque([(start, [start], 0)])
    visited = {start}

    while queue:
        current, path, cost = queue.popleft()

        if current == goal:
            return path, cost
        
        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor], cost + weight))

    return None, float('inf')

def dfs(graph, start, goal):
    stack = [(start, [start], 0)]
    visited = set()

    while stack:
        current, path, cost = stack.pop()

        if current == goal:
            return path, cost
        
        if current not in visited:
            visited.add(current)
            for neighbor, weight in reversed(graph.get(current, [])):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor], cost + weight))
    return None, float('inf')

def ucs(graph, start, goal):
    pq = PriorityQueue()
    pq.put((0, start, [start]))
    visited = {}

    while not pq.empty():
        cost, current, path = pq.get()
        if current == goal:
            return path, cost
        
        if current not in visited or cost < visited[current]:
            visited[current] = cost 
            for neighbor, weight in graph.get(current, []):
                new_cost = cost + weight
                if neighbor not in visited or new_cost < visited.get(neighbor, float('inf')):
                    pq.put((new_cost, neighbor, path + [neighbor]))
    return None, float('inf')


start_city = 'Arad'
end_city = 'Bucharest'

path_bfs, cost_bfs = bfs(romania_graph, start_city, end_city)
path_dfs, cost_dfs = dfs(romania_graph, start_city, end_city)
path_ucs, cost_ucs = ucs(romania_graph, start_city, end_city)

print("#BFS Result")
print("Path: ", "-> ".join(path_bfs))
print("Total Cost: ", cost_bfs, "\n")

print("#DFS Result")
print("Path: ", "-> ".join(path_dfs))
print("Total Cost: ", cost_dfs, "\n")

print("#UCS Result")
print("Path: ", "-> ".join(path_ucs))
print("Total Cost: ", cost_ucs, "\n")
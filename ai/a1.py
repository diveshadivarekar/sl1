from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

graph = {
    'A':['B', 'C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    order =[]

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return order

def dfs(graph, start, visited = None, order = None):
    if visited is None:
        visited = set()
    if order is None:
        order = []

    visited.add(start)
    order.append(start)

    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited, order)
    
    return order 



print(f"bfs -> {'->'.join(bfs(graph, 'A'))}")
print(f"dfs -> {'->'.join(dfs(graph, 'A'))}")

G = nx.Graph(graph)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='grey',node_size=2000, arrowsize=20)

plt.show()
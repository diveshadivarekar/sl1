import matplotlib.pyplot as plt
import networkx as nx
import heapq

graph = nx.Graph()

edges = {
    ('A', 'B'): 1,
    ('A', 'C'): 3,
    ('B', 'D'): 1,
    ('C', 'D'): 1,
    ('C', 'E'): 5,
    ('D', 'E'): 2
}

h = {
    'A':6, 'B': 4, 'C': 2, 'D': 1, 'E': 0
}

for (u,v), w in  edges.items():
    graph.add_edge(u,v, weight=w)

def astar(graph, start, goal):
    pq =[]
    heapq.heappush(pq, (h[start], 0, start, [start]))
    visited = set()

    while pq:
        est_total, cost, node, path = heapq.heappop(pq)
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)

        for nbr in graph.neighbors(node):
            g= cost + graph[node][nbr]['weight']
            f = h[node] + g
            heapq.heappush(pq, (f,g, nbr, path+[nbr]))

    return None

path = astar(graph, 'A', 'E')
print(path)

pos = nx.spring_layout(graph)

nx.draw(graph, pos, with_labels=True)

path_edges = list(zip(path, path[1:]))
nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color= "red")

plt.show()
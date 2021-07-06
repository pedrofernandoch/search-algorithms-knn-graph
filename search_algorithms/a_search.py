import numpy as np
from queue import PriorityQueue

def aSearch(graph, startVertex, endVertex, vertexArray):
    visited = [False] * len(graph)
    pq = PriorityQueue()
    pq.put((0, startVertex))
    path = []
    while pq.empty() == False:
        u = pq.get()[1]
        path.append(u)
        if u == endVertex:
            return path
        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                point1 = np.array([1] + vertexArray[v])
                point2 = np.array([1] + vertexArray[endVertex])
                manhattanDistance = abs(point1[0] - point2[0]) + abs(point2[1] - point2[1])
                pq.put((c + manhattanDistance, v))
    return None
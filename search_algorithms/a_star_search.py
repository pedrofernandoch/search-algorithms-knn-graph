import numpy as np
from queue import PriorityQueue

def aStarSearch(graph, startVertex, endVertex, vertexArray):
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
                point1 = np.array(vertexArray[v])
                point2 = np.array(vertexArray[endVertex])
                euclideanDistance = np.linalg.norm(point1 - point2)
                pq.put((c + euclideanDistance, v))
    return None
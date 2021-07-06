from queue import PriorityQueue

def bestFirstSearch(graph, startVertex, endVertex, vertexArray):
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
                pq.put((c, v))
    return None
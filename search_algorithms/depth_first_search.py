def depthFirstSearch(graph, startVertex, endVertex):
    stack = [(startVertex, [startVertex])]
    while stack:
        (vertex, path) = stack.pop()
        for node in set(list(map(lambda x: x[0], graph[vertex]))) - set(path):
            if node == endVertex:
                return path + [node]
            else:
                stack.append((node, path + [node]))
    return None
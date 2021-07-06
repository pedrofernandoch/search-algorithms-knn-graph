def breadthFirstSearch(graph, startNode, endNode, vertexArray):
    explored = []
    queue = [[startNode]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour[0])
                queue.append(new_path)
                if neighbour[0] == endNode:
                    return new_path
            explored.append(node)
    return None
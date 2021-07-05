def breadthFirstSearch(graph, startNode, endNode):
    explored = []
    queue = [[startNode]]
    # Loop to traverse the graph with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]
        # Condition to check if the current node is not visited
        if node not in explored:
            neighbours = graph[node]
            # Loop to iterate over the neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # Condition to check if the neighbour node is the endNode
                if neighbour == endNode:
                    return new_path
            explored.append(node)
    return None
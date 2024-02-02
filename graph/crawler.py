def crawl(graph, start, end, permitted_waypoints, already_visited, cost):
    """
    roams a graph from node to node
    ignoring already visited nodes
    TODO: visit every connection of one node which is more intelligent
    """
    if start == end:
        return cost
    else:
        for edge in graph.edges:
            if (edge.start == start and
                permitted_waypoints.count(edge.end) > 0 and
                    already_visited.count(edge.end) == 0):
                return crawl(
                        graph,
                        edge.end,
                        end,
                        permitted_waypoints,
                        already_visited.append(edge.end),
                        cost + edge.cost)

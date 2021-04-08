from Graph import *

costs = []
def crawl(graph, start, end, permitted_waypoints, already_visited, cost):
    if start == end:
        costs.append(cost)
    else:
        for edge in graph.edges:
            if edge.start == start and permitted_waypoints.count(edge.end) == 1 and already_visited.count(edge.end) == 0:
                crawl(graph, edge.end, end, permitted_waypoints, already_visited + [edge.end], cost + edge.cost)

############################################################
vertexes = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
edges = [
            ("1", 2, "2"), ("1", 4, "6"), ("1", 12, "7"), #(<start_node>, <int>, <end_node>)
            ("2", 10, "3"), ("2", 9, "7"),
            ("3", 2, "4"),
            ("4", 1, "5"),
            ("6", 11, "5"), ("6", 2, "8"),
            ("7", 15, "8"),
            ("8", 9, "5"), ("8", 1, "9"),
            ("9", 4, "3"), ("9", 7, "4"), ("9", 3, "7")
        ]
graph1 = Graph()
graph1.vertexes = vertexes
for edge in edges:
    graph1.edges.append(Edge(edge[0], edge[2], edge[1])) # Edge(start, end, cost)


crawl(graph1, "1", "7", graph1.vertexes, ["1"], 0)
print(costs)
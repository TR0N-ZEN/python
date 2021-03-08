import math
from Graph import *

class djikstra_tuple:
    def __init__(self, to, cost, predecessor):
        self.to = to #anything
        self.cost = cost #integer
        self.predecessor = predecessor #anything

def pick_shortest(discovered):
    shortest_path = djikstra_tuple("None", math.inf, "None")
    for path in discovered:
        if path.cost < shortest_path.cost:
            shortest_path = path
    return shortest_path

def update_discovered(graph, entered, discovered):
    shortest_path = entered[-1]
    for edge in graph.edges:
        A = edge.from
        B = edge.to
        if shortest_path.to == A: #found outgoing edge of newly entered node
            a_path_to_B_exists = False
            for discovered_path in discovered:
                if B == discovered_path.to:
                    a_path_to_B_exists = True
                    if discovered_path.cost > shortest_path.cost+edge.cost: # if path over newly entered node is cheapter/shorter replace the entry in discovered_path
                        discovered_path = djikstra_tuple(B, shortest_path.cost+edge.cost, A)
            if not(a_path_to_B_exists):
                discovered.append(djikstra_tuple(B, shortest_path.cost+edge.cost, A))

def djikstra(node, graph):
    entered = [] #contains djikstra_tuple
    discovered = [] #contains djikstra_tuple
    entered.append(djikstra_tuple(node, 0, "None"))
    update_discovered(graph, entered, discovered)
    while len(discovered) > 0:
        pick_shortest(discovered)
        update_discovered(graph, entered, discovered)
    return entered



############################################################
vertexes = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
edges = [
            ("1", 2, "2"), ("1", 4, "6"), ("1", 12, "7"), #(<from_node>, <int>, <to_node>)
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
    graph1.edges.append(Edge(edge[0], edge[2], edge[1])) # Edge(from, to, cost)

paths = djikstra("1", graph1)
print(paths)
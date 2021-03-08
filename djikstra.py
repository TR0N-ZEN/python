import math
from Graph import *

class djikstra_tuple:
    def __init__(self, to, cost, predecessor):
        self.to = to #anything
        self.cost = cost #integer
        self.predecessor = predecessor #anything

entered = [] #contains djikstra_tuple
discovered = [] #contains djikstra_tuple

vertexes = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
edges = [("1", 2, "2"), ("1", 4, "6"), ("1", 12, "7"), #(<from_node>, <int>, <to_node>)
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
    graph1.edges.append(Edge(edge[0], edge[2], edge[1])) # (from, to, cost)

entered.append(djikstra_tuple("1", 0, "None"))

def pick_shortest():
    shortest_path = djikstra_tuple("None", math.inf, "None")
    for path in discovered:
        if path.cost < shortest_path.cost:
            shortest_path = path
    return shortest_path

def update_discovered(shortest_path):
    for edge in graph1.edges:
        if shortest_path.to == edge.from: #found outgoing edge of newly entered node
            path_to = False
            for discovered_path in discovered:
                if edge.to == discovered_path.to:
                    path_to = True
                    if discovered_path.cost > shortest_path.cost+edge.cost:
                        discovered_path = djikstra_tuple(edge.to, shortest_path.cost+edge.cost, edge.from)
            if not(path_to):
                discovered.append(djikstra_tuple(edge.to, shortest_path.cost+edge.cost, edge.from))
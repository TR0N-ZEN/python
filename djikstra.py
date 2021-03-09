import math
from Graph import *

class djikstra_tuple:
    def __init__(self, to, cost, predecessor):
        self.to = to #anything
        self.cost = cost #integer
        self.predecessor = predecessor #anything
    def toString(tupel):
        return "("+tupel.to+", "+str(tupel.cost)+", "+tupel.predecessor+")"
    def copy(tupel):
        return djikstra_tuple(tupel.to, tupel.cost, tupel.predecessor)
    def list_toString(list):
        if list == []:
            return "List is empty."
        else:
            string = ""
            for tupel in list:
                string += djikstra_tuple.toString(tupel)
            return string

def pick_shortest(already_discovered_paths): # no sideeffects
    shortest_path = djikstra_tuple("None", math.inf, "None")
    for path in already_discovered_paths:
        if path.cost < shortest_path.cost:
            shortest_path = path
    return shortest_path

def has_shortest_path(node, shortest_paths): # no sideeffects
    for path in shortest_paths:
        if path.to == node:
            return True
    return False

def update_discovered(graph, shortest_paths, already_discovered_paths): #sideeffects
    print("already_discovered_paths(before): "+djikstra_tuple.list_toString(already_discovered_paths))
    new_shortest_path = shortest_paths[-1]
    print("shortest_path: "+djikstra_tuple.toString(new_shortest_path))
    already_discovered_paths.remove(new_shortest_path)
    for edge in graph.edges:
        # A = edge.start
        # B = edge.end
        if not(has_shortest_path(edge.end, shortest_paths)) and edge.start == new_shortest_path.to: #found outgoing edge of newly shortest_paths node
            a_path_to_B_exists_already = False #for each connection A-B, B is the other node of that connection
            for already_discovered_path in already_discovered_paths:
                if already_discovered_path.to == edge.end: #is there a path which has the same end as edge.end?
                    a_path_to_B_exists_already = True #there is
                    if already_discovered_path.cost > new_shortest_path.cost + edge.cost: # path over newly shortest_paths node is cheapter/shorter
                        already_discovered_path.predecessor = edge.start
                        already_discovered_path.cost = new_shortest_path.cost + edge.cost
            if not(a_path_to_B_exists_already): #has there been not already_discovered_paths path with an end at edge.end?
                already_discovered_paths.append(djikstra_tuple(edge.end, new_shortest_path.cost+edge.cost, edge.start))
    print("already_discovered_paths(after): "+djikstra_tuple.list_toString(already_discovered_paths))

def djikstra(start_node, graph):
    shortest_paths = [] #contains djikstra_tuples
    already_discovered_paths = [] #contains djikstra_tuples
    start_path = djikstra_tuple(start_node, 0, "None")
    already_discovered_paths.append(start_path)
    while len(already_discovered_paths) > 0:
        shortest_paths.append(pick_shortest(already_discovered_paths))
        update_discovered(graph, shortest_paths, already_discovered_paths)
    return shortest_paths



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
"""
print(graph1.vertexes)
for edge in graph1.edges:
    print(edge.start + " " + edge.end + " " + str(edge.cost))
"""
paths = djikstra("1", graph1)
"""
for path in paths:
    print_djikstra_tupel(path)
"""
class Edge:
    def __init__(self, from, to, cost):
        self.from = from
        self.to = to
        self.cost = cost
class Graph:
    def __init__(self):
        self.vertexes = [] #any datatype <x>
        self.edges = [] # (<x>, <int>, <x>) <=> (vertex_from, cost, vertex_to)
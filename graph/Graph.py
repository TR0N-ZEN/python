class Edge:
    def __init__(self, start, end, cost):
        self.start = start
        self.end = end
        self.cost = cost


class Graph:
    def __init__(self):
        self.vertexes = []  # any datatype <x>
        self.edges = []  # (<x>, <int>, <x>) <=> (vertex_from, cost, vertex_to)


# should maybe changed to be a list of edges
class Path:
    def __init__(self, start, end, intersections):
        self.start = start
        self.end = end
        self.intersections = intersections

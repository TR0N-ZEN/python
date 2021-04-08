from Graph import *
from Matrix import Matrix

graph = Graph()
############################################################
vertexes = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
edges = [
            ("1", 2, "2"), ("1", 4, "6"), ("1", 12, "7"), # (<start_node>, <int>, <end_node>)
            ("2", 10, "3"), ("2", 9, "7"),
            ("3", 2, "4"),
            ("4", 1, "5"),
            ("6", 11, "5"), ("6", 2, "8"),
            ("7", 15, "8"),
            ("8", 9, "5"), ("8", 1, "9"),
            ("9", 4, "3"), ("9", 7, "4"), ("9", 3, "7")
        ]
graph.vertexes = vertexes
for edge in edges:
    graph.edges.append(Edge(edge[0], edge[2], edge[1])) # Edge(start, end, cost)
matrix = Matrix(len(graph.vertexes), len(graph.vertexes))

for row in range(len(graph.vertexes)):
    for column in range(len(graph.vertexes)):
        value = f'{row}.{column}'
        matrix.enter(value, row, column)
        print(matrix.entry(row, column))

Matrix.print(matrix)
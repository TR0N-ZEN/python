"""
finds the cheapest path from each node to each other node
TODO: implement floyd warshall algorithm
"""


from Graph import Graph, Edge
from Matrix import Matrix

graph = Graph()
vertexes = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
edges = [
            # (<start_node>, <int>, <end_node>)
            ("1", 2, "2"), ("1", 4, "6"), ("1", 12, "7"),
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
    graph.edges.append(Edge(edge[0], edge[2], edge[1]))
matrix = Matrix(len(graph.vertexes), len(graph.vertexes))

for row in range(len(graph.vertexes)):
    for column in range(len(graph.vertexes)):
        value = f'{row}.{column}'
        matrix.en .enter(value, row, column)
        print(matrix.entry(row, column))

Matrix.print(matrix)

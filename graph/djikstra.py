import math


class djikstra_tuple:

    def __init__(self, to, cost, predecessor):
        self.to = to  # anything
        self.cost = cost  # integer
        self.predecessor = predecessor  # anything

    def toString(tupel):
        return f'({tupel.to}, {str(tupel.cost)}, {tupel.predecessor})'

    def list_toString(list):
        if list == []:
            return "List is empty."
        else:
            string = ""
            for tupel in list:
                string += djikstra_tuple.toString(tupel)
            return string

    def overwrite(tupel, to, cost, predecessor):
        tupel.to = to
        tupel.cost = cost
        tupel.predecessor = predecessor


def A_has_path_in_B(node, paths):  # no sideeffects
    for path in paths:
        if path.to == node:
            return True
    return False


def find_shortcut(edge, new_shortest_path, already_discovered_paths):
    """
    find outgoing edge of end node of the new shortest_paths
    side effects on already_discovered
    """
    if edge.start == new_shortest_path.to:
        if not A_has_path_in_B(edge.end, already_discovered_paths):
            already_discovered_paths.append(
                    djikstra_tuple(edge.end,
                                   new_shortest_path.cost+edge.cost,
                                   edge.start))
        else:
            for already_discovered_path in already_discovered_paths:
                # is there a path which has the same end as edge.end?
                # path over newly shortest_paths node is cheapter/shorter
                if already_discovered_path.to == edge.end and \
                   already_discovered_path.cost > new_shortest_path.cost + edge.cost:
                    djikstra_tuple.overwrite(
                            already_discovered_path,
                            edge.end,
                            new_shortest_path.cost + edge.cost,
                            edge.start)


def pick_shortest_path(already_discovered_paths):  # no sideeffects
    shortest_path = djikstra_tuple("None", math.inf, "None")
    for path in already_discovered_paths:
        if path.cost < shortest_path.cost:
            shortest_path = path
    return shortest_path


def update_discovered(graph, shortest_paths, already_discovered_paths):
    new_shortest_path = shortest_paths[-1]
    print(f'shortest_path: {djikstra_tuple.toString(new_shortest_path)}')
    already_discovered_paths.remove(new_shortest_path)
    for edge in graph.edges:
        if not A_has_path_in_B(edge.end, shortest_paths):
            find_shortcut(edge, new_shortest_path, already_discovered_paths)
    print(f'already_discovered_paths: {
        djikstra_tuple.list_toString(already_discovered_paths)}')


def djikstra(start_node, graph):  # no sideeffects
    shortest_paths = []  # contains djikstra_tuples
    already_discovered_paths = []  # contains djikstra_tuples
    start_path = djikstra_tuple(start_node, 0, "None")
    already_discovered_paths.append(start_path)
    while len(already_discovered_paths) > 0:
        shortest_paths.append(pick_shortest_path(already_discovered_paths))
        update_discovered(graph, shortest_paths, already_discovered_paths)
    return shortest_paths

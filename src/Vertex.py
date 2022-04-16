class Vertex:
    # Data type representing a vertex of a graph.
    # The list child_nodes keeps references to all adjacent nodes.
    # Variable parent is used for finding the shortest path between two node. (see breadth_first_search)

    def __init__(self, city_id, name):
        self.name = name
        self.city_id = city_id
        self.child_nodes = list()
        self.parent = None

    def set_child_nodes(self, child_nodes):
        self.child_nodes.append(child_nodes)

    def set_parent(self, parent):
        self.parent = parent
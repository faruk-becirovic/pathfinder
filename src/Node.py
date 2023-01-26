class Node:
    # Data type used for queue implementation, keeps reference to the node, the preceding node and succeeding node.

    def __init__(self, vertex):
        self.previous = None
        self.following = None
        self.vertex = vertex

    def get_vertex(self):
        return self.vertex

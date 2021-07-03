import csv


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


class Node:
    # Data type used for queue implementation, keeps reference to the node, the preceding node and succeeding node.

    def __init__(self, vertex):
        self.previous = None
        self.following = None
        self.vertex = vertex

    def get_vertex(self):
        return self.vertex


class Queue:
    # Implementation of queue data structure.
    # Uses FIFO principle, has methods to add node to the end, and to remove the node from the beginning.

    def __init__(self, first):
        self.first = first
        self.last = first
        self.length = 1

    def enqueue(self, n):
        self.last.following = n
        n.previous = self.last
        self.last = n
        self.length += 1
        if self.length == 1:
            self.first = n

    def dequeue(self):
        n = self.first
        self.first = self.first.following
        self.length -= 1
        return n


def read_graph():
    # Reeds data from two .csv files that represent the graph.
    # First file represents vertices.
    # Reeds city_id and city_name from the file, and uses these variables to construct Vertex type
    # Vertex type is stored in a list type.
    # Second represents edges.
    # Contains two integers per row representing two vertices connected by an edge.
    # When an edge is found the method adds reference of both method in each other.
    # References are stored as list attribute of Vertex type.
    # Returns list graph

    with open('cityName.csv') as first_file:
        graph = list()
        csv_reader = csv.reader(first_file, delimiter=',')
        line_count = 1
        for row in csv_reader:
            graph.append(Vertex(row[0], row[1]))
            line_count += 1

        with open('FromTo.csv') as second_file:
            csv_reader = csv.reader(second_file, delimiter=',')
            line_count = 1
            for row in csv_reader:
                for i in graph:
                    if i.city_id == row[0]:
                        for j in graph:
                            if j.city_id == row[1]:
                                i.set_child_nodes(j)
                                j.set_child_nodes(i)
                line_count += 1
    return graph


def breadth_first_search(visited, last, first):
    # Function implementing breadth-first search algorithm
    # Returns reference to the last node if the path is found.
    # Returns None if the path between two vertices is not found.
    queue = Queue(Node(first))
    visited.append(first)
    # Root node is added to the que and to list storing references to explored vertices.
    # The queue is looped through while loop as long as the que is not empty.

    while queue.length > 0:
        # The first vertex is retrieved from the queue.
        # Neighboring vertices are looped through.
        # All unexplored vertices are compared to the final node,
        # if the final node is found in the children nodes, the parent attribute of
        # the Vertex type is set to the current vertex and the reference to the final node is returned.
        # Vertices that are not final are added to visited list and added to the queue.
        # Returns reference to the final node,
        # Returns None if the path to the final node is not found.

        v = queue.dequeue().get_vertex()
        for i in v.child_nodes:
            if i not in visited:
                visited.append(i)
                i.set_parent(v)
                if i is last:
                    return last
                queue.enqueue(Node(i))

    return None


def find_city(name, graph):
    # Function used to find vertex in a graph based on the city name.
    # Return Vertex type
    # Prints message if city is not found.
    for i in graph:
        if i.name == name:
            print("Found city.")
            return i
    print("City not found, try again.")


def find_path():
    # Main function of the programme.
    graph = read_graph()
    city1 = None
    city2 = None

    # Takes first name from the user.
    while city1 is None:
        city1_name = input("Enter the name of the first city. ")
        city1 = find_city(city1_name, graph)

    # Takes second city name from the user.
    while city2 is None:
        city2_name = input("Enter the name of the second city. ")
        city2 = find_city(city2_name, graph)

    visited = list()

    # Calls breadth_first_search function on two end-point vertices.
    endpoint = breadth_first_search(visited, city1, city2)
    path = list()
    if endpoint is None:
        print("Path not found.")
    else:
        # The shortest path is found by tracking the parent attribute of Vertex type from one city Vertex to another.
        while endpoint.parent is not None:
            path.append(endpoint.name)
            endpoint = endpoint.parent

        for i in path:
            print(i, end="-")

        # Prints the resulting path.
        print(endpoint.name, end=", ")
        print("number of edges:", end=" ")
        print(path.__len__())


find_path()
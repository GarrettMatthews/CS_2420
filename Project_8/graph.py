"""
Weighted graph project

Garrett Matthews

"""

import math

class Graph(object):
    """A weighted graph adt"""

    def __init__(self):
        self.vertex = []
        self.graph = {}

    def add_vertex(self, label):
        """Adds a vertex to the graph, returns an error if not string, returns graph once added"""
        if not isinstance(label, str):
            raise ValueError("Error - vertex labels must be a string")
        self.vertex.append(label)
        self.graph[label] = []
        return Graph

    def add_edge(self, source, destination, weight):
        """Adds an edge with a weight between two vertexes"""
        if not isinstance(weight, (int, float)):
            raise ValueError("Weight must be an integer or a float")
        if source not in self.vertex or destination not in self.vertex:
            raise ValueError("All vertices must be present in graph before adding an edge")
        edge = (destination, float(weight))
        self.graph[source].append(edge)
        return Graph

    def get_weight(self, source, destination):
        """Returns the weight of an edge, returning infinity if no edge exists"""
        if source not in self.vertex or destination not in self.vertex:
            raise ValueError("All vertices must be added to the graph first")
        count = 0
        present = False
        for i in range(len(self.graph[source])):
            if self.graph[source][i][0] == destination:
                present = True
        if present:
            while self.graph[source][count][0] != destination:
                count += 1
            return self.graph[source][count][1]
        else:
            return math.inf

    def dfs(self, starting_vertex):
        """A depth first traversal for the graph"""
        if starting_vertex not in self.vertex:
            raise ValueError("Starting vertex must be in graph")
        depth = [starting_vertex]

        def recurse(vertex):
            """A helper recursive function for the dfs traversal"""
            if len(self.graph[vertex]) == 0:
                return None
            for i in range(len(self.graph[vertex])):
                if self.graph[vertex][i][0] not in depth:
                    depth.append(self.graph[vertex][i][0])
                    return recurse(self.graph[vertex][i][0])

        recurse(starting_vertex)
        return depth

    def bfs(self, starting_vertex):
        """Returns a breadth first traversal for the graph"""
        if starting_vertex not in self.vertex:
            raise ValueError("Starting vertex must be in graph")
        breadth = [starting_vertex]
        visited = [starting_vertex]

        def children(vertex):
            """Helper function for the bfs traversal, adds the children of the parent vertex"""
            if len(self.graph[vertex]) == 0:
                return None
            for i in range(len(self.graph[vertex])):
                if self.graph[vertex][i][0] not in breadth:
                    breadth.append(self.graph[vertex][i][0])

        def descend():
            """Helper function for the bfs traversal, descends the parent vertex"""
            for i in breadth:
                if i not in visited:
                    children(i)

        children(starting_vertex)
        descend()
        return breadth

    def dijkstra_shortest_path(self, source, destination=None):
        """
        Returns dijkstra's shortest path for between two vertices if a destination is supplied
        otherwise will return a dictionary for the shortest path between each vertex
        """
        if destination is None:
            return self.dij_dic(source)
        else:
            return self.dij_list(source, destination)

    def dij_dic(self, source):
        """Returns a dictionary of the shortest paths from the source to each vertex"""
        if source not in self.vertex:
            raise ValueError("Source vertex must be in graph")
        to_visit = []
        result = {}
        for i in self.vertex:
            if i != source:
                to_visit.append(i)
        for j in to_visit:
            result[j] = self.dij_list(source, j)
        return result

    def dij_list(self, source, destination):
        """Returns a tuple of the shortest path between two vertices (length, [path])"""
        if source not in self.vertex or destination not in self.vertex:
            raise ValueError("Both vertices must be in graph")
        path, distance = self.dijkstra(source, destination)
        dist_value = distance[destination]
        if dist_value == math.inf:
            path = []
        dij = (dist_value, path)
        return dij

    def dijkstra(self, source, destination):
        """Runs dijkstra's algorithm"""
        visited = []
        path = []
        distance = {}
        for i in self.vertex:
            distance[i] = math.inf
        for i in range(len(self.graph[source])):
            vertex = self.graph[source][i][0]
            if self.graph[source][i][1] < distance[vertex]:
                distance[vertex] = self.graph[source][i][1]
        visited.append(source)
        path.append(source)

        def find_smallest():
            """Finds the next vertex to be visited"""
            smallest = min(distance.values())
            vertices = vertex_finder(smallest)
            visit = [None]
            for k in vertices:
                if k not in visited:
                    if visit[0] is None:
                        visit[0] = k
                    else:
                        visit.append(k)
            return visit[0]

        def vertex_finder(value):
            """Finds the keys that correspond to a value within the distance dictionary"""
            keys = []
            items = distance.items()
            for j in items:
                if j[1] == value:
                    keys.append(j[0])
            return keys

        def recurse():
            """Recursive helper function for dijkstra's algorithm"""
            nxt = find_smallest()
            if nxt is not None:
                if len(self.graph[nxt]) > 0:
                    for key in range(len(self.graph[nxt])):
                        vert = self.graph[nxt][key][0]
                        if self.graph[nxt][key][1] < distance[vert]:
                            if distance[vert] == math.inf:
                                distance[vert] = self.graph[nxt][key][1]
                            else:
                                value = distance[vert] + self.graph[nxt][key][1]
                                distance[vert] = value
                    visited.append(nxt)
                    path.append(nxt)
                if nxt != destination:
                    return recurse()

        recurse()
        return path, distance

    def __str__(self):
        form = "numVertices: " + str(len(self.vertex)) + '\n'
        form += "Vertex " + '\t' + "Adjacency List" + '\n'
        for i in self.vertex:
            form += i + '\t' + '\t' + str(self.graph[i]) + '\n'
        return form

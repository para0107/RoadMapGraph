import random
from Iterator import IteratorBFS

class Graph:
    def __init__(self, directed, wheighted):
        self.neighbourhood_list = []
        self.vertices = []
        self.frec_ver = []
        for i in range(0,50):
            self.frec_ver.append(0)
        self.directed = directed  # check if it is directed or not
        self.wheight = wheighted
        self.wheight_list = []

    def set_directed_atribute(self):
        directed = random.randint(0, 1)
        self.directed = directed

    def set_frec_vertices(self):
        for i in range(0, 50):
            self.frec_ver = 0

    def set_graph_weight(self):
        self.wheight = random.randint(0, 1)

    def random_weights(self, param=None):
        if param is None:
            param = ()
        self.wheight = 1
        for item in self.neighbourhood_list:
            self.wheight_list[item] = random.randint(param[0], param[1])

    def set_weight(self, in_v, out_v, wheight):
        if self.wheight == 0:
            raise ValueError("This graph does not suppor wheights")
        else:
            for item in range(0, len(self.neighbourhood_list)):
                if self.neighbourhood_list[item] == (in_v,out_v):
                    w = random.randint(wheight[0], wheight[1])
                    self.wheight_list.append(w)

    def add_edge(self, in_vertex, ter_vertex):  # O(n) - Due to checking if vertices are in the graph.
        if (in_vertex, ter_vertex) in self.neighbourhood_list:
            raise ValueError("This edge is already in graph")
        if self.directed == 0 and (ter_vertex, in_vertex) in self.neighbourhood_list:
            raise ValueError("This edge is already in graph")
        for item in self.vertices:
            if item == in_vertex or item == ter_vertex:
                ok = 1
        self.neighbourhood_list.append((in_vertex, ter_vertex))
        if ok == 0:
            self.vertices.append(in_vertex)
            self.vertices.append(ter_vertex)
        w = random.randint(1, 10)
        if self.directed == 1 and self.wheight_list == 1:
            self.wheight_list.append(w)
#self.neighbourhood_list.append((in_vertex, ter_vertex))

    def add_vertex(self, vertex):  # O(1) - Appending to the vertices list.
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.frec_ver[vertex] = 1

    def remove_edge(self, in_vertex, ter_vertex):  # O(m) - Due to searching for the edge in the neighborhood list.
        if self.directed == 1:
            if (in_vertex, ter_vertex) not in self.neighbourhood_list:
                raise ValueError("This edge is not correct")
            else:
                self.neighbourhood_list.remove((in_vertex, ter_vertex))
                if self.frec_ver[in_vertex] == 1:
                    self.vertices.remove(in_vertex)
                if self.frec_ver[ter_vertex] == 1:
                    self.vertices.remove(ter_vertex)

        if self.directed == 0:
            if (ter_vertex, in_vertex) not in self.neighbourhood_list:
                if (in_vertex, ter_vertex) not in self.neighbourhood_list:
                    raise ValueError("This edge is not correct")
                else:
                    self.neighbourhood_list.remove((in_vertex, ter_vertex))
                    if self.frec_ver[in_vertex] == 1:
                        self.vertices.remove(in_vertex)
                    if self.frec_ver[ter_vertex] == 1:
                        self.vertices.remove(ter_vertex)
            else:
                if (in_vertex, ter_vertex) in self.neighbourhood_list:
                    raise ValueError("This graph is oriented")
                self.neighbourhood_list.remove((ter_vertex, in_vertex))
                if self.frec_ver[in_vertex] == 1:
                    self.vertices.remove(in_vertex)
                if self.frec_ver[ter_vertex] == 1:
                    self.vertices.remove(ter_vertex)

    def remove_vertex(self, vertex):  # O(n*m) - Removing edges associated with the vertex and then removing the
        # vertex itself.
        if vertex not in self.vertices:
            raise ValueError("This vertex is not correct")
        self.vertices.remove(vertex)
        self.frec_ver[vertex] = 0
        for item in self.neighbourhood_list:
            if item[0] == vertex or item[1] == vertex:
                self.neighbourhood_list.remove(item)

    def remove_vertex_but_with_specifications(self, vertex):
        if vertex not in self.vertices:
            raise ValueError("This vertex is not correct")
        for item in self.neighbourhood_list:
            if item[0] == vertex or item[1] == vertex:
                self.neighbourhood_list.remove(item)
        for index in range(vertex, len(self.vertices) + 1):
            for item in self.neighbourhood_list:
                if item[0] == self.vertices[index]:
                    item[0] = item[0] - 1
                if item[1] == self.vertices[index]:
                    item[1] = item[1] - 1
            self.vertices[index] = self.vertices[index] - 1
        self.vertices.remove(vertex)

    def create_random(self, n, m, wheights_range):  # O(n*m) - Generating m random edges.
        if m > n * (n - 1):
            raise ValueError("This is not correct")
        self.vertices.clear()
        self.neighbourhood_list.clear()
        for item in range(1, n + 1):
            self.vertices.append(item)
        while m:
            v1 = random.randint(1, n)
            v2 = random.randint(1, n)
            if (v1, v2) in self.neighbourhood_list:
                continue
            elif v1 == v2:
                continue
            elif self.directed == 0 and (v2, v1) in self.neighbourhood_list:
                continue
            else:
                self.neighbourhood_list.append((v1, v2))
                m = m - 1
                self.frec_ver[v1] += 1
                self.frec_ver[v2] += 1
                if self.directed == 1:
                    if self.wheight == 1:
                        if wheights_range == (0, 0):
                            wheights_range = random.randint(0, 10)
                        self.set_weight(v1, v2, wheights_range)

    def get_n(self):  # O(1) - Just returns the length of vertices list.
        return len(self.vertices)

    def get_m(self):  # O(1) - Just returns the length of neighborhood list.
        return len(self.neighbourhood_list)

    def deg(self, vertex):  # O(m) - Traverses through neighborhood list to find degree of vertex.
        in_bound = 0
        out_bound = 0
        if vertex not in self.vertices:
            raise ValueError("This vertex is not correct")
        else:
            if self.directed == 1:
                for item in self.neighbourhood_list:
                    if item[0] == vertex:
                        in_bound += 1
                    if item[1] == vertex:
                        out_bound += 1
                return in_bound + out_bound
            else:
                bound = 0
                for item in self.neighbourhood_list:
                    if item[0] == vertex or item[1] == vertex:
                        bound += 1
                return bound

    def is_edge(self, vert1, vert2):  # O(m) - Searches for the edge in the neighborhood list.
        if vert1 not in self.vertices or vert2 not in self.vertices:
            raise ValueError("This vertices are not correct")
        if self.directed == 1:
            if (vert1, vert2) in self.neighbourhood_list:
                return True
            else:
                return False
        else:
            if(vert1, vert2) in self.neighbourhood_list or (vert2, vert1) in self.neighbourhood_list:
                return True
            else:
                return False

    def outbound_edges(self, vertex):  # O(m) - Collecting all edges where the given vertex is the starting vertex.
        if self.directed == 1:
            outbound_list = []
            for item in self.neighbourhood_list:
                if item[0] == vertex:
                    outbound_list.append(item[1])
            return outbound_list
        else:
            outbound = []
            for item in self.neighbourhood_list:
                if item[0] == vertex or item[1] == vertex:
                    outbound.append(item)

    def inbound_edges(self, vertex):  # O(m) - Collecting all edges where the given vertex is the ending vertex.
        inbound_list = []
        for item in self.neighbourhood_list:
            if item[1] == vertex:
                inbound_list.append(item[0])
        return inbound_list

    def copy_graph(self):  # O(m) - Copies the neighborhood list.
        new_list_neighbourhood = self.neighbourhood_list[:]
        return new_list_neighbourhood

    def __str__(self):  # O(n + m) - Constructs strings for vertices and edges.
        vertices_str = "Vertices: " + ', '.join(str(v) for v in self.vertices)
        edges_str = "Edges: " + ', '.join(
            f"({in_vertex}, {ter_vertex})" for (in_vertex, ter_vertex) in self.neighbourhood_list)
        wheight_str = "weights: " + " , ".join(str(w) for w in self.wheight_list if self.wheight == 1)
        return vertices_str + "\n" + edges_str + "\n" + wheight_str

    def iter_vertex(self, start_vertex):
        return IteratorBFS(self, start_vertex)

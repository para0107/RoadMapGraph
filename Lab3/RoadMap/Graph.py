class Graph:
    def __init__(self):
        self.neighbourhood_list = []
        self.vertices = []
        self.weight_list = []
        self.roads = []

    def set_weight(self, in_vertice, out_vertice, weight):
        for index in range(len(self.neighbourhood_list)):
            if self.neighbourhood_list[index] == (in_vertice, out_vertice):
                self.weight_list.insert(index, weight)

    def add_edge(self, in_vertex, ter_vertex):
        # if (in_vertex, ter_vertex) in self.neighbourhood_list:
        #     raise ValueError("This edge is already in the graph")
        self.neighbourhood_list.append((in_vertex, ter_vertex))
        if in_vertex not in self.vertices:
            self.vertices.append(in_vertex)
        if ter_vertex not in self.vertices:
            self.vertices.append(ter_vertex)

    def add_vertex(self, vertex):
        if vertex in self.vertices:
            raise ValueError("This vertexz already exists")
        else:
            self.vertices.append(vertex)

    def remove_edge(self, in_vertex, ter_vertex):
        if (in_vertex, ter_vertex) not in self.neighbourhood_list:
            raise ValueError("This vertex is not in the graph")
        else:
            self.neighbourhood_list.remove((in_vertex, ter_vertex))
        found1 = 0
        found2 = 0
        for item in self.neighbourhood_list:
            if item[0] == in_vertex:
                found1 = 1
            if item[1] == ter_vertex:
                found2 = 1
        if found1 == 0:
            self.vertices.remove(in_vertex)
        if found2 == 0:
            self.vertices.remove(ter_vertex)

    def remove_vertex(self, vertice):
        self.vertices.remove(vertice)
        for item in self.neighbourhood_list:
            if item[0] == vertice:
                self.neighbourhood_list.remove(item)
            if item[1] == vertice:
                self.neighbourhood_list.remove(item)

    def get_vertices_n(self):
        return len(self.vertices)

    def get_edges_m(self):
        return len(self.neighbourhood_list)

    def get_degree(self, vertex):
        degree = 0
        if vertex not in self.vertices:
            raise ValueError("This vertex is not correct")
        for item in self.neighbourhood_list:
            if item[0] == vertex or item[1] == vertex:
                degree += 1
        return degree

    def __str__(self):
        vertices_str = f"Vertices of the graph: {self.vertices}\n"
        neighborhood_str = f"Neighborhood list: {self.neighbourhood_list}\n"
        weights_str = f"The weight of the each edge:{self.weight_list}"
        return vertices_str + neighborhood_str + weights_str

    def is_edge(self, in_vertex, ter_vertex):
        if (in_vertex, ter_vertex) in self.neighbourhood_list:
            return True
        return False

    def add_road_map(self, road_name, directed, intersection):
        if road_name not in self.roads:
            self.roads.append(road_name)
        path = []
        for item in intersection:
            path.append(item)
        for index in range(len(self.roads)):
            if self.roads[index] == road_name:
                self.roads.append(path)
            # in the self.roads, I have added the name of the road and a list of all vertices
        for i in range(len(intersection) - 1):
            start_vertex, _ = intersection[i]
            end_vertex, cost = intersection[i + 1]
            if start_vertex not in self.vertices:
                self.vertices.append(start_vertex)
            if end_vertex not in self.vertices:
                self.vertices.append(end_vertex)
            self.add_edge(start_vertex, end_vertex)
            if directed != 'T':
                self.add_edge(end_vertex, start_vertex)
                if cost != 0:
                    self.weight_list.append(cost)
            if cost != 0:
                self.weight_list.append(cost)
            # here, I have added in my neighbourhood list the edges and the vertices
            # in my vertices list

    def read_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                road_name = parts[0]
                road_type = parts[1]
                intersections = [(pair.split(';')[0], int(pair.split(';')[1])) for pair in parts[2:]]
                self.add_road_map(road_name, road_type, intersections)

    def floyd_warshall(self):
        # Initialize the distance matrix with infinity for unreachable pairs
        dist_matrix = [[float('inf')] * len(self.vertices) for _ in range(len(self.vertices))]

        # Initialize the diagonal with zeros (distance from a vertex to itself is zero)
        for i in range(len(self.vertices)):
            dist_matrix[i][i] = 0

        # Fill in the distance matrix with the weights of existing edges
        for i, (u, v) in enumerate(self.neighbourhood_list):
            weight = self.weight_list[i]
            u_index = self.vertices.index(u)
            v_index = self.vertices.index(v)
            dist_matrix[u_index][v_index] = weight

        # Apply Floyd-Warshall algorithm
        for k in range(len(self.vertices)):
            for i in range(len(self.vertices)):
                for j in range(len(self.vertices)):
                    dist_matrix[i][j] = min(dist_matrix[i][j], dist_matrix[i][k] + dist_matrix[k][j])

        return dist_matrix

    def shortest_distance(self, start_vertex, finish_vertex):
        if start_vertex not in self.vertices or finish_vertex not in self.vertices:
            raise ValueError("Start or finish vertex not found in the graph")

        dist_matrix = self.floyd_warshall()
        start_index = self.vertices.index(start_vertex)
        finish_index = self.vertices.index(finish_vertex)

        return dist_matrix[start_index][finish_index]

    def shortest_distance_with_road_change_cost(self, start_vertex, finish_vertex, road_change_cost):
        if start_vertex not in self.vertices or finish_vertex not in self.vertices:
            raise ValueError("Start or finish vertex not found in the graph")
        dist_matrix = self.floyd_warshall()
        start_index = self.vertices.index(start_vertex)
        finish_index = self.vertices.index(finish_vertex)
        # Add the road change cost to each entry in the distance matrix
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if dist_matrix[i][j] != float('inf'):
                    dist_matrix[i][j] += road_change_cost
        return dist_matrix[start_index][finish_index]




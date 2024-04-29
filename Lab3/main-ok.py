from Graph import *


lst = []

print("[1] : Set if the graph is directed or is not: \n"
      "[2] : Set if the graph is wheighted or is not: \n"
      "[3] : Randomly generate the graph: \n"
      "[4] : Set a specific wheight of a vertex: \n"
      "[5] : Set the random wheights of the graph:\n"
      "[6] : Add an edge to the graph: \n"
      "[7] : Add a vertex to the graph: \n"
      "[8] : Remove an edge from the graph: \n"
      "[9] : Remove a vertex from the graph: \n"
      "[10] : Get the number of vertices: \n"
      "[11] : Get the number of edges: \n"
      "[12] : Get the degree of a vertex: \n"
      "[13] : Check if the given edge exists in graph: \n"
      "[14] : Copy the graph into a new one:\n"
      "[15] : Iterate through the graph: \n"
      "[16] : Print the graph.")

option = int(input("An option"))
d = random.randint(0, 1)
w = random.randint(0, 1)
graph = Graph(d,w)
while option:
    if option == 1:
        graph.set_directed_atribute()
        print("This graph is directed? \n", graph.directed)

    if option == 2:
        graph.set_graph_weight()
        print("This graph is wheighted? \n", graph.wheight)

    if option == 3:
        n = int(input("Number of vertices is: "))
        m = int(input("Number of edges is: "))
        inf = int(input("The lower bound of range for weight: "))
        sup = int(input("The upper bpund of range for weight:"))
        graph.create_random(n, m, (inf, sup))

    if option == 4:
        # x = int(input("The first vertex to add weight to: "))
        # y = int(input("The second vertex to add vertex to:"))
        # w = int(input("The desired weight of the edge: "))
        # graph.set_weight(x, y, w)
        continue

    if option == 5:

        p = int(input("The range of generated weight: "))
        graph.random_weights(p)

    if option == 6:
        v1 = int(input("The vertex to the edge: "))
        v2 = int(input("The vertex of the edge: "))
        graph.add_edge(v1, v2)

    if option == 7:
        v = int(input("The vertex is:"))
        graph.add_vertex(v)

    if option == 8:
        v1 = int(input("The vertex to the edge: "))
        v2 = int(input("The vertex of the edge: "))
        graph.remove_edge(v1, v2)

    if option == 9:
        v = int(input("The vertex is:"))
        graph.remove_vertex(v)

    if option == 10:
        print(graph.get_n(),"\n")

    if option == 11:
        print((graph.get_m()), "\n")

    if option == 12:
        v = int(input("The vertex is:"))
        print(graph.deg(v))

    if option == 13:
        v1 = int(input("The vertex to the edge: "))
        v2 = int(input("The vertex of the edge: "))
        print(graph.is_edge(v1, v2))

    if option == 14:
        new_graph = graph.copy_graph()

    if option == 15:
        v = int(input("The starting vertex:"))
        graph.iter_vertex(v)

    if option == 16:
        print(graph)

    option = int(input("\n Another option:"))


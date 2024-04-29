from Graph import *

road = Graph()

road.read_from_file(filename='roads_shortened.txt')
# print (road)
# print("\n",len(road.neighbourhood_list))
# print("\n", len(road.weight_list))
distances = road.shortest_distance('I1','I3')
print(distances)

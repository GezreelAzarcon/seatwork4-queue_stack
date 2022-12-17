# from graph import City, load_graph

# nodes, graph = load_graph("C:/Users/borgy/Desktop/python/seatwork4-queue_stack/uk/roadmap.dot", City.from_dict)

# nodes["edinburgh"]


# print(graph)

# def sort_by(neighbors, strategy):
#     return sorted(neighbors.items(), key=lambda item: strategy(item[1]))

# def by_distance(weights):
#     return float(weights["distance"])

# for neighbor, weights in sort_by(graph[nodes["london"]], by_distance):
#     print(f"{weights['distance']:>3} miles, {neighbor.name}")

import networkx as nx
from graph import City, load_graph, dijkstra_shortest_path

nodes, graph = load_graph("C:/Users/borgy/Desktop/python/seatwork4-queue_stack/uk/roadmap.dot", City.from_dict)

city1 = nodes["london"]
city2 = nodes["edinburgh"]

def distance(weights):
    return float(weights["distance"])

for city in dijkstra_shortest_path(graph, city1, city2, distance):
    print(city.name)


def weight(node1, node2, weights):
    return distance(weights)

def by_distance(weights):
     return float(weights["distance"])

print("==========================================================================")
print()
for city in nx.dijkstra_path(graph, city1, city2, weight):
    print(city.name)

#
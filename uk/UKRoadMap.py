from graph import City, load_graph

nodes, graph = load_graph("C:/Users/borgy/Desktop/python/seatwork4-queue_stack/uk/roadmap.dot", City.from_dict)

nodes["london"]


print(graph)

def sort_by(neighbors, strategy):
    return sorted(neighbors.items(), key=lambda item: strategy(item[1]))

def by_distance(weights):
    return float(weights["distance"])

for neighbor, weights in sort_by(graph[nodes["london"]], by_distance):
    print(f"{weights['distance']:>3} miles, {neighbor.name}")
import os
from util import *


def cheapest_insertion(coords):

    # list of all nodes (airports) not visited yet (all excluding the first one since we start from there)
    nodes_left = list(range(1, len(coords), 1))
    route = [0, 0]  # list of all nodes (airports) already in the minimal spanning tree
    route_length = 0

    while nodes_left:
        best_node = None
        best_route = None
        best_route_length = None
        for i in range(0, len(route)-1, 1):
            for node in nodes_left:
                length = route_length \
                         - euclidean_distance(coords[route[i]], coords[route[i+1]]) \
                         + euclidean_distance(coords[route[i]], coords[node]) \
                         + euclidean_distance(coords[node], coords[route[i+1]])
                if best_node is None or length < best_route_length:
                    best_node = node
                    best_route = route.copy()
                    best_route.insert(i+1, node)
                    best_route_length = length
        route = list(best_route)
        route_length = best_route_length
        del nodes_left[nodes_left.index(best_node)]

    return route, route_length


if __name__ == "__main__":

    if len(sys.argv) != 2:
        raise ValueError("\n\tUsage: python cheapest_insertion.py <path to instance>\n"
                         "\tTry:   python cheapest_insertion.py ./data/eins.txt")
    else:
        file_path = sys.argv[1]

    # load instance
    if os.path.exists(file_path):
        coords = read_instance_from_file(file_path)
    else:
        raise FileNotFoundError(f"File not found: {file_path}")

    print(f"Executing cheapest insertion algorithm on {len(coords)} airports...")
    route, route_length = measure_runtime(cheapest_insertion, coords)
    print(f"Resulting route when using the cheapest insertion algorithm has a length of {route_length:.2f}:"
          f"\n \t{[value + 1 for value in route]}")

    print("Plotting network graph...")
    plot_coordinates(coords, route)

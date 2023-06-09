import os
from util import *


def nearest_neighbour(coords):
    """
    Nearest neighbour algorithm
    coords[0] is the starting node
    :param coords: List of coordinate tuples of the airports
    :return: route, route_length
    """

    # list of all airports not visited yet (all excluding the first one since we start from there)
    nodes_left = list(range(1, len(coords), 1))
    current_node = 0
    # list of all nodes (airports) already in the route
    route = [0]
    route_length = 0

    # iterate
    while nodes_left:
        best_node = None
        best_route = None
        best_route_length = None

        for node in nodes_left:
            new_route = route.copy()
            new_route.append(node)
            new_route_length = route_length + euclidean_distance(coords[current_node], coords[node])
            if best_node is None or new_route_length < best_route_length:
                best_node = node
                best_route = new_route.copy()
                best_route_length = new_route_length

        route = list(best_route)
        route_length = best_route_length
        current_node = best_node
        del nodes_left[nodes_left.index(best_node)]

    # add starting airport to complete route
    route_length += euclidean_distance(coords[route[-1]], coords[0])
    route.append(0)

    return route, route_length


if __name__ == "__main__":

    if len(sys.argv) != 2:
        raise ValueError("\n\tUsage: python nearest_neighbour.py <path to instance>\n"
                         "\tTry:   python nearest_neighbour.py ./data/eins.txt")
    else:
        file_path = sys.argv[1]

    # load instance
    if os.path.exists(file_path):
        coords = read_instance_from_file(file_path)
    else:
        raise FileNotFoundError(f"File not found: {file_path}")

    print(f"Executing nearest neighbour algorithm on {len(coords)} airports...")
    route, route_length = measure_runtime(nearest_neighbour, coords)
    print(f"Resulting route when using the nearest neighbour algorithm has a length of {route_length:.2f}:"
          f"\n \t{[value + 1 for value in route]}")

    print("Plotting network graph...")
    plot_coordinates(coords, route)

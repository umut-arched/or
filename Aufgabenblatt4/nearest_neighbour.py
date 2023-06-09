from util import *
import os


def nearest_neighbour(coords):
    """
    Nearest neighbour algorithm
    coords[0] is the starting node
    :param coords: List of coordinate tuples of the airports
    :return: route, route_length
    """

    # list of all airports not visited yet (all excluding the first one since we start from there)
    airports_left = list(range(1, len(coords), 1))
    current_airport = 0
    route = [0]
    route_length = 0

    # iterate
    while len(airports_left) != 0:

        # get all distances to other airports from current airport
        distances = []
        for airport in airports_left:
            distances.append(euclidean_distance(coords[current_airport], coords[airport]))

        # find shortest distance to another airport
        min_dist = distances.index(min(distances))

        # add distance to next airport to route length
        route_length += distances[min_dist]

        # add next airport to route
        route.append(airports_left[min_dist])

        # set next airport to current airport for next iteration
        current_airport = airports_left[min_dist]

        # delete next airport from list of airports left
        del airports_left[min_dist]

        # add distance back to first airport if all airports have been visited
        if not airports_left:
            route_length += euclidean_distance(coords[current_airport], coords[0])

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

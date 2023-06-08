from util import *


def nearest_neighbour(coords):

    # get list of all airports except the first one (index 0) since we start from there
    airports_left = list(range(1, len(coords), 1))
    current_airport = 0
    route = [0]

    # iterate
    while len(airports_left) != 0:
        distances = []
        for airport in airports_left:
            distances.append(euclidean_distance(coords[current_airport], coords[airport]))
        min_dist = distances.index(min(distances))
        route.append(airports_left[min_dist])
        current_airport = airports_left[min_dist]
        del airports_left[min_dist]

    route.append(0)

    return route


if __name__ == "__main__":

    coords = read_instance_from_file("./data/zwei.txt")
    route = measure_runtime(nearest_neighbour, coords)
    print(f"Resulting route when using the nearest neighbour algorithm:\n \t{[value + 1 for value in route]}")

    plot_coordinates(coords, route)


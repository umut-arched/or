import os
import importlib
from util import *


def two_opt(coords, route, iteration_depth):
    """
    Execute the two_opt algorith for a maximum iteration depth
    :param coords: List of coordinate tuples of the airports
    :param route: initial route calculated by one of the start heuristics
    :param iteration_depth: maximum number of iterations
    :return: route, route_length
    """

    improvement = True
    best_route = init_route
    best_route_length = get_route_length(coords, init_route)

    iteration = 0
    # iterate as long as improvements are made or the iteration depth is reached
    while improvement and iteration < iteration_depth:
        improvement = False
        iteration += 1

        # select first edge (here, an edge has start node i and end node i + 1)
        for i in range(1, len(route) - 2):
            # select second edge (start node j, end node j + 1)
            for j in range(i + 1, len(route)):
                # skip iteration if edges are adjacent since adjacent edges can't be swapped
                if j - i == 1:
                    continue

                new_route = list(route)
                # reverse the selected edges
                new_route[i:j] = route[j - 1 : i - 1 : -1]
                new_route_length = get_route_length(coords, new_route)
                if new_route_length < best_route_length:

                    best_route_length = new_route_length
                    best_route = new_route
                    improvement = True

        route = best_route

    if not improvement:
        if iteration-1 == 0:
            print("Input route already is optimized")
        else:
            print(f"Optimized route found after {iteration-1} iterations")
    else:
        print(f"Iteration limit of {iteration} iterations has been reached")

    return best_route, best_route_length


if __name__ == "__main__":

    # check for correct number of command line args
    if len(sys.argv) != 4:
        raise ValueError("\n\tUsage: python two_opt.py <path to instance> <start heuristic> <iteration depth>\n"
                         "\tTry:   python two_opt.py ./data/eins.txt nearest_neighbour 1000")
    else:
        file_path = sys.argv[1]
        # convert string like "./nearest_neighbour.py" to "nearest_neighbour"
        start_heuristic = sys.argv[2].replace("\\", "/").split("/")[-1].replace(".py", "")
        iteration_depth = sys.argv[3]

    # check if start heuristic is available and import function
    possible_start_heuristics = ["nearest_neighbour", "cheapest_insertion"]
    if start_heuristic not in possible_start_heuristics:
        raise ValueError(f"\n\tUsage: python two_opt.py <path to instance> <start heuristic>\n"
                         f"\t Possible start heuristics: {possible_start_heuristics}")
    else:
        module = importlib.import_module(start_heuristic)
        function = getattr(module, start_heuristic)

    # load instance
    if os.path.exists(file_path):
        coords = read_instance_from_file(file_path)
    else:
        raise FileNotFoundError(f"File not found: {file_path}")

    # get initial route and route_length
    init_route, init_route_length = function(coords)

    print(f"Initial route has length of {init_route_length:.2f} using {start_heuristic.replace('_', ' ')} algorithm")

    print(f"Executing 2-opt algorithm for {iteration_depth} iterations")
    optimized_route, optimized_route_length = measure_runtime(two_opt, coords, init_route, 1000)

    print(f"Resulting route when using the 2-opt algorithm has a length of {optimized_route_length:.2f}, "
          f"improvement of {init_route_length-optimized_route_length:.2f}:"
          f"\n \t{[value + 1 for value in optimized_route]}")

    print("Plotting optimized network graph...")
    plot_coordinates(coords, optimized_route)

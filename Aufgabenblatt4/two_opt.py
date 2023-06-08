import sys
import os
import importlib
from util import *
from nearest_neighbour import *


def two_opt(coords, route, iteration_depth):

    improvement = True
    best_route = init_route
    best_route_length = get_route_length(coords, init_route)

    iteration = 0
    while improvement and iteration < iteration_depth:
        improvement = False
        iteration += 1

        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1:
                    # skip iteration if edges are adjacent
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
        print(f"Optimal route found after {iteration} iterations.")
    else:
        print(f"Iteration limit of {iteration} iterations has been reached. Exiting.")

    return best_route, best_route_length


if __name__ == "__main__":

    if len(sys.argv) != 3:
        raise ValueError("\n\tUsage: python two_opt.py <path to instance> <start heuristic>\n"
                         "\tTry:   python two_opt.py ./data/eins.txt nearest_neighbour")
    else:
        file_path = sys.argv[1]
        start_heuristic = sys.argv[2]

    # check if start heuristic is eligible and import function
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

    print(init_route)
    print(init_route_length)

    optimized_route, optimized_route_length = measure_runtime(two_opt, coords, init_route, 1000)

    print(optimized_route)
    print(optimized_route_length)
    plot_coordinates(coords, optimized_route)

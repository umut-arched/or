import sys
import os
import importlib
from util import *
from nearest_neighbour import *


def two_opt(coords, init_route, iteration_depth):

    def get_edges(route):
        """
        Returns all edges of a given route
        :param r: given route
        :return: list of tuples representing edges
        """
        edges = []
        for i in range(len(route)-1):
            edges.append((init_route[i], init_route[i+1]))
        return edges

    def get_non_adjacent_edge_pairs(edges):
        """
        Get all pairs of non-adjacent edges that might be considered for edge-swapping
        :param edges:
        :return:
        """
        pairs = []
        for i in range(len(edges)-2):
            for j in range(i+2, min(i+len(edges)-1, len(edges)), 1):
                pairs.append((edges[i], edges[j]))
        return pairs

    def swap_edges(old_route, pair):
        """
        Create a new route by swapping two edges

        Process given input ((a, b), (c, d)):
            - iterate through initial route until node a is reached
            - from node a, jump to node c
            - from node c, iterate backwards through the initial route until node b is reached
            - from node b, jump to node d
            - from node d, iterate forward through the initial route until node a is reached to complete the route

        :param pair: a pair of edges to be swapped ((a, b), (c, d)) where a, b, c, d are nodes (airports)
        :return: new route
        """
        a = pair[0][0]
        b = pair[0][1]
        c = pair[1][0]
        d = pair[1][1]
        new_route = []
        i = 0  # index to iterate through old_route
        while 1<2:
            new_route.append(old_route[i])
            if old_route[i] == a:
                break
            i += 1
        i = old_route.index(c)
        while 1 < 2:
            new_route.append(old_route[i])
            if old_route[i] == b:
                break
            i -= 1
        i = old_route.index(d)
        while 1 < 2:
            new_route.append(old_route[i])
            if old_route[i] == 0:
                break
            i += 1

        return new_route

    # edges = get_edges(init_route)
    # print(edges)
    # pairs = get_non_adjacent_edge_pairs(edges)
    # print(pairs)
    # print(swap_edges(init_route, pairs[1]))

    i = 0
    current_route = init_route
    current_route_length = get_route_length(coords, init_route)
    while i < iteration_depth:
        i += 1

        # initialize variables to save best route and best length for this iteration
        best_route = None
        best_route_length = None

        # iterate through all edge pairs that can be swapped
        pairs = get_non_adjacent_edge_pairs(get_edges(current_route))
        for pair in pairs:
            new_route = swap_edges(current_route, pair)
            new_route_length = get_route_length(coords, new_route)

            # update best_route if new_route is better than best_route and current_route
            if new_route_length < current_route_length:
                if best_route_length is None:
                    best_route = new_route
                    best_route_length = new_route_length
                elif new_route_length < best_route_length:
                    best_route = new_route
                    best_route_length = new_route_length

        # break if no better route could be found, else update current_route and continue loop
        if best_route is None:
            break
        else:
            current_route = best_route
            current_route_length = best_route_length

    return current_route, current_route_length


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

    optimized_route, optimized_route_length = two_opt(coords, init_route, 3)

    print(optimized_route)
    print(optimized_route_length)
    plot_coordinates(coords, optimized_route)




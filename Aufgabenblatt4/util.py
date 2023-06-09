"""
This script contains helper functions used in other scripts of this project.
It does not need to be called individually.

To use in other scripts use either:
    from util.py import <function name>, <function name>, ...
    from util.py import *
"""

import sys
import math
import matplotlib.pyplot as plt
import time


def read_instance_from_file(path):
    """
    Reads coordinates from an instance
    :param path: path to instance text file containing the coordinates
    :return: list of tuples containing x- and y-coordinates of airports where index 0 is the first airport
    """
    filename = path.replace('\\', '/').split('/')[-1]
    print(f"Reading instance: {filename}")
    x_coords = []
    y_coords = []
    with open(path, 'r') as file:
        for line in file:
            line = line.replace("\n", "").split(" ")
            x_coords.append(float(line[1]))
            y_coords.append(float(line[2]))
    return list(zip(x_coords, y_coords))


def euclidean_distance(a, b):
    """
    Calculate euclidean distance
    :param a: Tuple of coordinates of point a
    :param b: Tuple of coordinates of point b
    :return: euclidian distance
    """
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


def get_route_length(coords, route):
    """
    Calculates the length of a given route
    :param coords: Coordinates of airports
    :param route: Order of airports in the route
    :return: length of route
    """
    route_length = 0
    for i in range(len(route)-1):
        route_length += euclidean_distance(coords[route[i]], coords[route[i+1]])
    return route_length


def plot_coordinates(coords, edges=None, index_shift=True):
    """
    Visualize the network using matplotlib
    :param coords: Coordinates of airports
    :param edges: either route (List[int]) or minimal spanning tree (List[Tuple[int]])
    :param index_shift: if True, add 1 to all indices to get indices like in the instances (starting at 1)
    :return:
    """

    # extract x- and y-coordinates
    x_coords = [coord[0] for coord in coords]
    y_coords = [coord[1] for coord in coords]

    # Plot edges between vertices
    if edges:
        # if edges is list of integers: plot route
        if isinstance(edges, list) and all(isinstance(item, int) for item in edges):
            for i in range(len(edges) - 1):
                start = edges[i]
                end = edges[i + 1]
                plt.plot([x_coords[start], x_coords[end]], [y_coords[start], y_coords[end]], '#6093f7', zorder=2)
        # if edges is list of tuples: plot route
        elif isinstance(edges, list) and all(isinstance(item, tuple) for item in edges):
            for start, end in edges:
                plt.plot([x_coords[start], x_coords[end]], [y_coords[start], y_coords[end]], '#6093f7', zorder=2)

    # Plot the coordinates
    plt.scatter(x_coords, y_coords, s=200, c='#1132d6', zorder=1)

    # Add labels and title
    plt.xlabel('X Coordinates')
    plt.ylabel('Y Coordinates')
    plt.title('Airport network graph')

    # Add indices to the points
    for i, coord in enumerate(coords):
        plt.text(coord[0], coord[1], str(i + 1 if index_shift else i), ha='center', va='center', c='w', zorder=3)

    # Show the plot
    plt.show()


def measure_runtime(func, *args, **kwargs):
    """
    Measures the runtime of a function call.
        - call function, returns its return value
        - print runtime to command line
    :param func: function to measure runtime of
    :param *args: parameters of function to pass
    :return: return value of function
    """
    start_time = time.perf_counter()
    return_value = func(*args, **kwargs)
    end_time = time.perf_counter()
    runtime = (end_time - start_time) * 1000  # in milliseconds
    print(f"Runtime of {func.__name__}: {runtime:.2f} ms")
    return return_value


if __name__ == "__main__":
    """
    The following code is only used for testing. The algorithm scripts only import the functions.
    
    However, the script can be called in order to read instances and have the lists containing x- and y-coordinates
    printed:
    
        Usage:      python util.py <path to instance>
        Example:    python util.py /data/eins.txt
    """

    clargs = sys.argv

    if len(clargs) == 1:
        # default
        path = "./data/eins.txt"
    elif len(clargs) == 2:
        path = sys.argv[1]
    else:
        ValueError("Usage: python util.py <path to instance>")

    coords = read_instance_from_file(path)
    print(coords)

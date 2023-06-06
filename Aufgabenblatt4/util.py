"""
To use in other scripts:
from util.py import read_instance_from_file
"""

import sys
import math


def read_instance_from_file(path):
    """
    Reads coordinates from an instance
    :param path: path to instance text file containing the coordinates
    :return: list of tuples containing x- and y-coordinates of airports where index 0 is the first airport
    """
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


def calculate_distances(x_coords, y_coords):
    pass


if __name__ == "__main__":
    """
    The following code is only used for testing. The algorithm scripts only access the read_instance_from_file function.
    
    However, the script can be called in order to read instances and have the lists containing x- and y-coordinates
    printed:
    
    Usage: python util.py <path to instance>
    
    Example: python util.py /data/eins.txt
    """

    args = sys.argv

    if len(args) == 1:
        # default
        path = "./data/eins.txt"
    elif len(args) == 2:
        path = sys.argv[1]
    else:
        ValueError("Usage: python util.py <path to instance>")

    coords = read_instance_from_file(path)

    print(coords)
    print(coords[0][1])

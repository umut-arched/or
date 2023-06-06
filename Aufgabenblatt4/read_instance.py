
import sys

def read_instance_from_file(path):
    """
    Reads coordinates from an instance
    :param path: path to instance text file containing the coordinates
    :return: x_coords and y_coords list where x_coords[0] is the x-coordinate of airport with index 1 in the file
    """
    x_coords = []
    y_coords = []
    with open(path, 'r') as file:
        for line in file:
            line = line.replace("\n", "").split(" ")
            x_coords.append(float(line[1]))
            y_coords.append(float(line[2]))
    return x_coords, y_coords


if __name__ == "__main__":
    """
    The following code is only used for testing. The algorithm scripts only access the read_instance_from_file function.
    
    However, the script can be called in order to read instances and have the lists containing x- and y-coordinates
    printed:
    
    Usage: python read_instance.py <path to instance>
    
    Example: python read_instance.py /data/eins.txt
    """

    args = sys.argv
    if len(args) != 2:
        ValueError("Usage: python read_instance.py <path to instance>")

    x_coords, y_coords = read_instance_from_file(sys.argv[1])

    print(x_coords)
    print(y_coords)

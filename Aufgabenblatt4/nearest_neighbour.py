from util import read_instance_from_file, euclidean_distance
import matplotlib.pyplot as plt


def plot_coordinates(coords, route=None):
    """
    Visualize the network using matplotlib
    :param coords: Coordinates of airports
    :return:
    """

    # extract x- and y-coordinates
    x_coords = [coord[0] for coord in coords]
    y_coords = [coord[1] for coord in coords]

    # Plot the coordinates
    plt.scatter(x_coords, y_coords)

    # Add labels and title
    plt.xlabel('X Coordinates')
    plt.ylabel('Y Coordinates')
    plt.title('Scatter Plot of Coordinates')

    # Add indices to the points
    for i, coord in enumerate(coords):
        plt.text(coord[0], coord[1], str(i), ha='center', va='bottom')

    # Plot edges between vertices
    for i in range(len(route) - 1):
        start = route[i]
        end = route[i + 1]
        plt.plot([x_coords[start], x_coords[end]], [y_coords[start], y_coords[end]], 'r')

    # Show the plot
    plt.show()


def nearest_neighbour(coords):

    # get list of all airports except the first one (index 0) since we start from there
    airports_left = list(range(1, 10, 1))
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

    coords = read_instance_from_file("./data/eins.txt")
    route = nearest_neighbour(coords)
    print(route)

    plot_coordinates(coords, route)

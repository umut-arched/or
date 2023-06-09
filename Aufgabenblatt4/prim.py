import os
from util import *


def prim(coords):

    # list of all nodes (airports) not visited yet (all excluding the first one since we start from there)
    nodes_left = list(range(1, len(coords), 1))
    mst_nodes = [0]  # list of all nodes (airports) already in the minimal spanning tree
    mst_edges = []  # list of all edges (a, b) in the minimal spanning tree where a, b are nodes (airports)
    mst_length = 0

    while nodes_left:
        best_node = None
        best_edge = None
        best_dist = None
        for mst_node in mst_nodes:
            for node in nodes_left:
                dist = euclidean_distance(coords[mst_node], coords[node])
                if best_node is None or dist < best_dist:
                    best_node = node
                    best_edge = (mst_node, node)
                    best_dist = dist
        mst_nodes.append(best_node)
        mst_edges.append(best_edge)
        mst_length += best_dist
        del nodes_left[nodes_left.index(best_node)]

    return mst_edges, mst_length


if __name__ == "__main__":

    if len(sys.argv) != 2:
        raise ValueError("\n\tUsage: python prim.py <path to instance>\n"
                         "\tTry:   python prim.py ./data/eins.txt")
    else:
        file_path = sys.argv[1]

    # load instance
    if os.path.exists(file_path):
        coords = read_instance_from_file(file_path)
    else:
        raise FileNotFoundError(f"File not found: {file_path}")

    print(f"Executing prim's algorithm on {len(coords)} airports...")
    mst, mst_length = measure_runtime(prim, coords)
    print(f"Resulting MST when using prim's algorithm has a length of {mst_length:.2f} and contains edges:"
          f"\n \t{[(value[0] + 1, value[1] + 1) for value in mst]}")

    plot_coordinates(coords)

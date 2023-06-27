import sys
from util import *






if __name__ == "__main__":

    if len(sys.argv) != 2:
        raise ValueError("\n\tUsage: python greedy_knapsack.py <path to instance>\n"
                         "\tTry:   python greedy_knapsack.py ./instances/kp_0_1_10_50.txt")
    else:
        instance_path = sys.argv[1]

    num_items, weights, values, capacity = read_instance_from_file(instance_path, print_instance=True)
    items = create_item_classes(weights, values)

    # sort items by profitability
    sorted_items = sorted(items, key=lambda item: item.profitability)

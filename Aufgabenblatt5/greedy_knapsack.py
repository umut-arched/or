import sys
from util import *


def greedy_knapsack(items):

    # sort items by profitability
    sorted_items = sorted(items, key=lambda item: item.profitability)

    # init objective values
    used_capacity = 0
    total_value = 0
    items_in_knapsack = []

    # iterate over all items
    for i, item in enumerate(sorted_items):
        used_capacity += item.weight
        if used_capacity >= capacity:
            # remove last weight (the one that exceeds the capacity)
            used_capacity -= item.weight
            # break loop to not add current item and its value to the result
            break
        items_in_knapsack.append(item)
        total_value += item.value

    return items_in_knapsack, total_value, used_capacity


if __name__ == "__main__":

    if len(sys.argv) != 2:
        raise ValueError("\n\tUsage: python greedy_knapsack.py <path to instance>\n"
                         "\tTry:   python greedy_knapsack.py ./instances/kp_0_1_10_50.txt")
    else:
        instance_path = sys.argv[1]

    num_items, weights, values, capacity = read_instance_from_file(instance_path, print_instance=True)
    items = create_item_classes(weights, values)

    items_in_knapsack, total_value, used_capacity = greedy_knapsack(items)

    print("\nGreedy knapsack result:")
    print(f"  Total value:   {total_value}")
    print(f"  Used capacity: {used_capacity}/{capacity}")
    print("\nItems in knapsack:")
    for item in items_in_knapsack:
        print(f"  {item}")

    pass




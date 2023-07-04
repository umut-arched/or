"""
Usage: python greedy_knapsack_continuous.py <path to instance>
Try:   python greedy_knapsack_continuous.py ./instances/kp_0_1_10_50.txt
"""

import sys
from util import *


def greedy_knapsack_continuous(items, capacity):
    """
    Solves a continuous greedy knapsack problem
    It works exactly like the binary greedy knapsack solution with the exception that the item that exceeds the capacity
    is partially put into the knapsack.
    :param items: list of item objects to calculate the optimal solution for
    :param capacity: the capacity of the knapsack
    :return: items_in_knapsack, total_value, used_capacity
    """

    # sort items by profitability
    sorted_items = sorted(items, key=lambda item: item.profitability, reverse=True)

    # init objective values
    used_capacity = 0
    total_value = 0
    items_in_knapsack = []

    # iterate over all items
    for i, item in enumerate(sorted_items):
        used_capacity += item.weight
        # check if capacity is exceeded
        if used_capacity >= capacity:

            # get percentage of last item that would fit
            exceeding_capacity = used_capacity - capacity
            item_percentage = 1 - (1 / item.weight * exceeding_capacity)

            # catch edge cases
            if item_percentage == 1:
                # just add the last item if it fits completely
                items_in_knapsack.append(item)
                total_value += item.value
                break
            elif item_percentage == 0:
                # don't add another item if the knapsack is at full capacity
                break
            else:
                # create partial item
                partial_item = Item(f"{item.id} ({item_percentage*100}%)", item.weight*item_percentage,
                                    item.value*item_percentage)

                # add new partial item to knapsack and its value to the total value
                items_in_knapsack.append(partial_item)
                total_value += partial_item.value
                # set the used_capacity = capacity since it's fully used up
                used_capacity = capacity

            # break loop
            break

        items_in_knapsack.append(item)
        total_value += item.value

    return items_in_knapsack, total_value, used_capacity


if __name__ == "__main__":

    if len(sys.argv) != 2:
        raise ValueError("\n\tUsage: python greedy_knapsack_continuous.py <path to instance>\n"
                         "\tTry:   python greedy_knapsack_continuous.py ./instances/kp_0_1_10_50.txt")
    else:
        instance_path = sys.argv[1]

    num_items, weights, values, capacity = read_instance_from_file(instance_path, print_instance=True)
    items = create_item_classes(weights, values)

    items_in_knapsack, total_value, used_capacity = greedy_knapsack_continuous(items, capacity)

    print("\nGreedy knapsack (continuous) result:")
    print(f"  Total value:   {total_value}")
    print(f"  Used capacity: {used_capacity}/{capacity}")
    print("\nItems in knapsack:")
    for item in items_in_knapsack:
        print(f"  {item}")

    pass




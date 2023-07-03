"""
Usage: python dynamic_knapsack_b.py <path to instance>
Try:   python dynamic_knapsack_b.py ./instances/kp_0_1_10_50.txt
"""

import sys
from util import *
from greedy_knapsack import greedy_knapsack
from dynamic_knapsack import print_table


def dynamic_knapsack_integer_profit(items, capacity, do_print_table=False):

    num_items = len(items)
    _, max_profit, _ = greedy_knapsack(items, capacity)
    max_profit *= 2

    # create and fill table
    table = [[0] * (max_profit + 1) for _ in range(num_items + 1)]

    # initialize table
    for k in range(max_profit+1):
        if k > 0:
            table[0][k] = capacity+1

    for i, item in enumerate(items, start=1):
        for k in range(max_profit + 1):
            if k - item.value >= 0 and table[i - 1][k - item.value] + item.weight <= capacity:
                table[i][k] = min(table[i - 1][k - item.value] + item.weight, table[i - 1][k])
            else:
                table[i][k] = table[i - 1][k]

    if do_print_table:
        print_table(table)


    items_in_knapsack = []
    total_value = used_capacity = 0
    i, k = num_items, max_profit
    while table[i][k] == table[i][k-1]:
        k -= 1
    k -= 1
    while i > 0 and k > 0:
        while table[i][k] == table[i-1][k]:
            i -= 1
        items_in_knapsack.append(items[i-1])
        total_value += items[i-1].value
        used_capacity += items[i-1].weight
        k -= items[i-1].value
        i -= 1

    return items_in_knapsack, total_value, used_capacity


if __name__ == "__main__":

    if len(sys.argv) != 2:
        raise ValueError("\n\tUsage: python dynamic_knapsack_integer_profit.py <path to instance>\n"
                         "\tTry:   python dynamic_knapsack_integer_profit.py ./instances/kp_0_1_10_50.txt")
    else:
        instance_path = sys.argv[1]

    num_items, weights, values, capacity = read_instance_from_file(instance_path, print_instance=True)
    items = create_item_classes(weights, values)

    items_in_knapsack, total_value, used_capacity = dynamic_knapsack_integer_profit(items, capacity)

    print("\nDynamic knapsack (integer profit) result:")
    print(f"  Total value:   {total_value}")
    print(f"  Used capacity: {used_capacity}/{capacity}")
    print("\nItems in knapsack:")
    for item in items_in_knapsack:
        print(f"  {item}")

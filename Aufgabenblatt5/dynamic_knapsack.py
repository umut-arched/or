"""
Usage: python dynamic_knapsack.py <path to instance>
Try:   python dynamic_knapsack.py ./instances/kp_0_1_10_50.txt
"""

import sys
from util import *


def print_table(table):
    """
    Prints the table generated by dynamic knapsack.
    Table can get vary large for high capacity
    """

    print()
    num_rows = len(table)
    num_cols = len(table[0])

    column_widths = [max(len(str(item)) for item in column) for column in zip(*table)]

    # Print column indices and separator
    print(' ' * max(column_widths), end=' | ')
    for col_idx in range(num_cols):
        print(f'{col_idx:{column_widths[col_idx]}}', end=' ')
    print()

    separator = '-' * (max(column_widths))

    print(separator, end=' |')
    for col_idx in range(num_cols):
        print(separator, end='')
    print()

    for row_idx, row in enumerate(table):
        # Print row index and separator
        print(f'{row_idx:{max(column_widths)}}', end=' | ')

        for item, width in zip(row, column_widths):
            print(f'{item:{width}}', end=' ')
        print()


def dynamic_knapsack(items, do_print_table=False):

    num_items = len(items)

    # create and fill table
    table = [[0] * (capacity + 1) for _ in range(num_items + 1)]
    for i, item in enumerate(items, start=1):
        for j in range(1, capacity + 1):
            if item.weight > j:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = max(table[i - 1][j], item.value + table[i - 1][j - item.weight])

    if do_print_table:
        print_table(table)

    # get solution from table
    items_in_knapsack = []
    used_capacity = total_value = 0
    i, j = num_items, capacity
    while i > 0:
        if table[i - 1][j] < table[i][j]:
            items_in_knapsack.append(items[i - 1])
            total_value += items[i - 1].value
            used_capacity += items[i - 1].weight
            j -= items[i - 1].weight
        i -= 1

    return items_in_knapsack, total_value, used_capacity


if __name__ == "__main__":

    if len(sys.argv) != 2:
        raise ValueError("\n\tUsage: python dynamic_knapsack.py <path to instance>\n"
                         "\tTry:   python dynamic_knapsack.py ./instances/kp_0_1_10_50.txt")
    else:
        instance_path = sys.argv[1]

    num_items, weights, values, capacity = read_instance_from_file(instance_path, print_instance=True)
    items = create_item_classes(weights, values)

    items_in_knapsack, total_value, used_capacity = dynamic_knapsack(items, True)

    print("\nDynamic knapsack result:")
    print(f"  Total value:   {total_value}")
    print(f"  Used capacity: {used_capacity}/{capacity}")
    print("\nItems in knapsack:")
    for item in items_in_knapsack:
        print(f"  {item}")

    pass
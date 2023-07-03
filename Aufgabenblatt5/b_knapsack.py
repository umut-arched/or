import sys
from util import *
from dynamic_knapsack import print_table


def dynamic_knapsack_integer_profit(items, do_print_table=False):
    num_items = len(items)
    max_profit = max(item.value for item in items)  # Upper bound on optimal profit

    # create and fill table
    table = [[capacity + 1] * (max_profit + 1) for _ in range(num_items + 1)]
    table[0][0] = 0

    for i, item in enumerate(items, start=1):
        for k in range(max_profit + 1):
            if k - item.value >= 0 and table[i - 1][k - item.value] + item.weight <= capacity:
                table[i][k] = min(table[i - 1][k - item.value] + item.weight, table[i - 1][k])
            else:
                table[i][k] = table[i - 1][k]

    if do_print_table:
        print_table(table)

    # get solution from table
    items_in_knapsack = []
    total_value = used_capacity = 0
    i, k = num_items, max_profit
    while i > 0 and k > 0:  #i, k fuer den Meme Effekt :p
        if table[i][k] != table[i - 1][k]:
            items_in_knapsack.append(items[i - 1])
            total_value += items[i - 1].value
            used_capacity += items[i - 1].weight
            k -= items[i - 1].value
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

    items_in_knapsack, total_value, used_capacity = dynamic_knapsack_integer_profit(items, True)

    print("\nDynamic knapsack (integer profit) result:")
    print(f"  Total value:   {total_value}")
    print(f"  Used capacity: {used_capacity}/{capacity}")
    print("\nItems in knapsack:")
    for item in items_in_knapsack:
        print(f"  {item}")

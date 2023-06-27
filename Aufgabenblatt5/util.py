


def read_instance_from_file(path, print_instance=False):
    """
    Read an instance from a file
    :param path: Path to the instance file
    :param print_instance: If true, information about instance will be printed
    :return: num_items, weights, values, capacity
    """
    filename = path.replace('\\', '/').split('/')[-1]
    print(f"Reading instance: {filename}")
    # read file
    with open(path, 'r') as file:
        for line_number, line in enumerate(file):
            line = line.replace("\n", "").split(" ")
            if line_number == 0:
                # get number of items from first line
                num_items = int(line[0])
            elif line_number == 1:
                # get item weights from second line
                weights = list(map(int, line))
            elif line_number == 2:
                # get item values from third line
                values = list(map(int, line))
            elif line_number == 3:
                # get capacity from fourth line
                capacity = int(line[0])

    # print instance
    if print_instance:
        print(f"Number of items: {num_items}")
        print(f"Item weights:    {weights}")
        print(f"Item values:     {values}")
        print(f"Capacity:        {capacity}")

    return num_items, weights, values, capacity


if __name__ == "__main__":
    read_instance_from_file("./instances/whoopdeedoo.txt", print_instance=True)

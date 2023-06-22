import argparse
import random
import os


def parse_arguments(print_args=False):

    parser = argparse.ArgumentParser(
        description="Parameters",
        usage="%(prog)s [-n number] [-s seed] [-lb lower_bound] [-ub upper_bound] [-C capacity_percentage] [-f filename]"
    )

    # Define the arguments
    parser.add_argument("-n", type=int, required=True, help="Number of items")
    parser.add_argument("-s", type=int, required=False, default=0, help="Random seed")
    parser.add_argument("-lb", type=float, required=False, default=1, help="Lower bound for weights")
    parser.add_argument("-ub", type=float, required=False, default=10, help="Upper bound for weights")
    parser.add_argument("-c", type=float, required=False, default=50, help="Percentage of capacity to total weight")
    parser.add_argument("-f", required=False, default=None, help="Name of the generated txt file")

    # Parse the arguments
    args = parser.parse_args()

    # Access the argument values
    num_items = args.n
    seed = args.s
    lower_bound = args.lb
    upper_bound = args.ub
    capacity_percentage = args.c
    filename = args.f
    if filename is None:
        filename = f"kp_{num_items}_{seed}_{lower_bound}_{upper_bound}_{capacity_percentage}"

    if print_args:
        print(f"Number of items: {num_items}")
        print(f"Random seed: {seed}")
        print(f"Lower bound for weights: {lower_bound}")
        print(f"Upper bound for weights: {upper_bound}")
        print(f"Capacity percentage: {capacity_percentage}")
        print(f"Filename of generated file: {filename}.txt")

    return num_items, seed, lower_bound, upper_bound, capacity_percentage, filename


if __name__ == "__main__":

    # get arguments
    num_items, seed, lower_bound, upper_bound, capacity_percentage, filename = parse_arguments(True)

    # set random seed
    random.seed(seed)

    # generate random weights and values
    weights = [random.randint(lower_bound, upper_bound) for _ in range(num_items)]
    values = [random.randint(lower_bound, upper_bound) for _ in range(num_items)]

    # calculate capacity
    capacity = sum(weights)*capacity_percentage/100

    # generate txt file
    script_directory = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(f"{script_directory}/instances", exist_ok=True)
    with open(f"{script_directory}/instances/{filename}.txt", "w") as file:
        file.write(str(num_items) + "\n")
        file.write(" ".join(map(str, weights)) + "\n")
        file.write(" ".join(map(str, values)) + "\n")
        file.write(str(capacity))



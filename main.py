from Knapsack import *


def main():
    item1 = Item(1, 3, 25)
    item2 = Item(2, 2, 20)
    item3 = Item(3, 1, 15)
    item4 = Item(4, 4, 40)
    item5 = Item(5, 5, 50)

    capacity = 6

    items_in = []
    items_out = []

    items_in.extend((item1, item2, item3))
    items_out.extend((item4, item5))

    knapsack = Knapsack(items_in, items_out, capacity)
    print("Knapsack before perturbation 1:")
    knapsack.print_items()

    knapsack.perturb1()
    print("Knapsack after perturbation 1:")
    knapsack.print_items()

    # knapsack.perturb1()
    # print("Knapsack after perturbation 2:")
    # knapsack.print_items()


if __name__ == "__main__":
    main()

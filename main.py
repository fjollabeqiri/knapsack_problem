from Knapsack import *


def main():
    item1 = Item(1, 3, 25)
    item2 = Item(2, 2, 20)
    item3 = Item(3, 1, 15)
    item4 = Item(4, 9, 30)
    item5 = Item(5, 6, 10)
    item6 = Item(6, 8, 55)
    item7 = Item(7, 7, 50)
    item8 = Item(8, 5, 40)
    item9 = Item(9, 10, 35)
    item10 = Item(10, 4, 60)

    capacity = 15

    items_in = []
    items_out = []

    items_in.extend((item1, item2, item3, item4))
    items_out.extend((item5, item6, item7, item8, item9, item10))

    knapsack = Knapsack(items_in, items_out, capacity)
    print("Knapsack initial solution:")
    knapsack.print_items()

    knapsack.perturb1()
    print("Knapsack after perturbation 1:")
    knapsack.print_items()

    print("Knapsack after perturbation 2:")
    knapsack.perturb2()
    knapsack.print_items()


if __name__ == "__main__":
    main()

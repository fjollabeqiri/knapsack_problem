import random
from typing import List


class Item:
    def __init__(self, item_id, weight, value):
        self.id = item_id
        self.weight = weight
        self.value = value


class Knapsack:
    def __init__(self, items_in, items_out, capacity):
        self.items_in = items_in
        self.items_out = items_out
        self.capacity = capacity

    def check_feasibility(self, items):
        w = 0
        for item in items:
            w = w + item.weight
            if w > self.capacity:
                return False

        if w > self.capacity:
            return False
        else:
            return True

    def print_items(self):
        items_in_knapsack_before = ""
        for item in self.items_in:
            items_in_knapsack_before = items_in_knapsack_before + str(item.id) + ", "
        items_in_knapsack_before = items_in_knapsack_before[:-2]

        items_in_knapsack_before = items_in_knapsack_before + " | "
        for item in self.items_out:
            items_in_knapsack_before = items_in_knapsack_before + str(item.id) + ", "

        items_in_knapsack_before = items_in_knapsack_before[:-2]
        print(items_in_knapsack_before)

    def perturb1(self):
        feasible = False
        items_removed: List[Item] = []
        items_in_updated: List[Item] = []
        items_out_updated: List[Item] = []

        while not feasible:
            # remove n random elements
            items_in_copy = self.items_in.copy()
            items_out_copy = self.items_out.copy()
            items_removed = []
            self.remove_items(items_in_copy, items_out_copy, items_removed)

            counter = 0
            while not feasible:
                if counter <= 10:
                    # add m random elements
                    items_in_updated = items_in_copy.copy()
                    items_out_updated = items_out_copy.copy()
                    self.add_items(items_out_copy, items_in_updated, items_out_updated)
                    feasible = self.check_feasibility(items_in_updated)
                    counter = counter + 1
                else:
                    break

        for item in items_removed:
            items_out_updated.append(item)

        self.items_in = items_in_updated
        self.items_out = items_out_updated

    def remove_items(self, items_in_copy, items_out_copy, items_removed):
        no_of_items_in = len(self.items_in)
        rand_no_of_items_out = random.randint(1, no_of_items_in)
        rand_items_out = random.sample(list(range(0, no_of_items_in)), rand_no_of_items_out)
        rand_items_out.sort(reverse=True)
        for rand in rand_items_out:
            items_removed.append(items_in_copy[rand])
            items_in_copy.pop(rand)

    def add_items(self, items_out_copy, items_in_updated, items_out_updated):
        no_of_items_out = len(self.items_out)
        rand_no_of_items_in = random.randint(1, no_of_items_out)
        rand_items_in = random.sample(list(range(0, no_of_items_out)), rand_no_of_items_in)
        rand_items_in.sort(reverse=True)
        for rand in rand_items_in:
            items_in_updated.append(items_out_copy[rand])
            items_out_updated.remove(items_out_copy[rand])

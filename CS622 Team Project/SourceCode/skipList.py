import random
from heapSort import heapSort
from mergeSort import MergeSort

class Node:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * (level + 1)

class skipListClass:
    def __init__(self, max_level, p):
        self.max_level = max_level
        self.p = p
        self.header = self.create_node(self.max_level, -1)
        self.level = 0

    def create_node(self, lvl, key):
        return Node(key, lvl)

    def random_level(self):
        lvl = 0
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    def insert(self, key):
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        lvl = self.random_level()

        if lvl > self.level:
            for i in range(self.level + 1, lvl + 1):
                update[i] = self.header
            self.level = lvl

        new_node = self.create_node(lvl, key)

        for i in range(lvl + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def delete(self, key):
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current and current.key == key:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            while self.level > 0 and self.header.forward[self.level] is None:
                self.level -= 1
                
    def search(self, key):
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
        current = current.forward[0]
        if current and current.key == key:
            return current
        return None

    def display_list(self):
        # print("Skip List:")
        for lvl in range(self.level + 1):
            print(f"Level {lvl}: ", end=" ")
            node = self.header.forward[lvl]
            while node:
                print(node.key, end=" ")
                node = node.forward[lvl]
            print("")
    
    def heap_sort(self):
        arr = []
        current = self.header.forward[0]
        while current:
            arr.append(current.key)
            current = current.forward[0]

        heap_sorter = heapSort()
        heap_sorter.sort(arr)

        self.__init__(self.max_level, self.p)
        for key in arr:
            self.insert(key)

    def get_last_item(self):
        current = self.header
        while current.forward[0]:
            current = current.forward[0]
        return current.key if current != self.header else None

    def selection_sort(self):
        current = self.header.forward[0]
        while current:
            smallest = current
            next_node = current.forward[0]
            while next_node:
                if next_node.key < smallest.key:
                    smallest = next_node
                next_node = next_node.forward[0]
            current.key, smallest.key = smallest.key, current.key
            current = current.forward[0]

    def merge_sort(self):
            arr = []
            current = self.header.forward[0]
            while current:
                arr.append(current.key)
                current = current.forward[0]

            sorter = MergeSort()
            sorter.mergeSort(arr, 0, len(arr) - 1)

            self.__init__(self.max_level, self.p)
            for key in arr:
                self.insert(key)

if __name__ == "__main__":
    # Example usage
    skip_list = skipList(3, 0.5)
    skip_list.insert(12)
    skip_list.insert(19)
    skip_list.insert(17)
    skip_list.insert(26)
    skip_list.insert(21)
    skip_list.insert(3)
    skip_list.insert(6)
    skip_list.insert(7)
    skip_list.insert(9)
    skip_list.insert(25)
    skip_list.delete(17)

    print("Original list:")
    skip_list.display_list()
    
    temp=skip_list
    temp.heap_sort()
    print("Sorted list by heap_sort:")
    skip_list.display_list()
    
    temp=skip_list
    temp.merge_sort()
    print("Sorted list by merge_sort:")
    skip_list.display_list()

    print("Search for 19:", skip_list.search(19))
    print("Search for 15:", skip_list.search(15))

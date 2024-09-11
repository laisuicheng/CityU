from heapSort import heapSort
from mergeSort import MergeSort

class Node:
    def __init__(self, data):
        self.data = data

class SimpleArrayClass:
    def __init__(self):
        self.items = []

    def insert_item(self, item):
        self.items.append(item)

    def delete_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def get_last_item(self):
        if self.items:
            return self.items[-1]
        return None

    def print_items(self):
        print(self.items)

    def selection_sort(self):
        for i in range(len(self.items)):
            min_idx = i
            for j in range(i+1, len(self.items)):
                if self.items[min_idx] > self.items[j]:
                    min_idx = j
            self.items[i], self.items[min_idx] = self.items[min_idx], self.items[i]

    def heap_sort(self):
        heap_sorter = heapSort()
        heap_sorter.sort(self.items)
        
    def merge_sort(self):
        sorter = MergeSort()
        sorter.mergeSort(self.items, 0, len(self.items) - 1)
from heapSort import heapSort
from mergeSort import MergeSort

class Node:
    def __init__(self, key):
        self.key = key
        self.forward = None

class LinkedListClass:
    def __init__(self):
        self.header = None

    def print_items(self):
        cur = self.header
        arr = []
        while cur:
            arr.append(str(cur.key))
            cur = cur.forward
        print(' -> '.join(arr))

    def insert_item(self,key):
        if key is not None:
            newNode=Node(key)
            newNode.forward=self.header
            self.header=newNode
                
    def search(self, key):
        cur = self.header
        if cur is None:
            return None
        while cur and cur.forward:
            if cur.key == key:
                return cur
            cur = cur.forward
        return None

    def delete_item(self, key):
        cur = self.header
        prev = None
        if cur is not None and cur.key == key:
            self.header = cur.forward
            return

        while cur:
            if cur.key == key:
                prev.forward = cur.forward
                break
            prev, cur = cur, cur.forward

    def find_smallest(self, node):
        cur = node
        if cur is None:
            return None
        smallest = cur.key
        smallestNode = cur
        while cur:
            if cur.key < smallest:
                smallest = cur.key
                smallestNode = cur
            cur = cur.forward
        return smallest, smallestNode

    def get_last_item(self):
            cur = self.header
            lastitem = None
            while cur:
                lastitem = cur.key
                cur = cur.forward
            return lastitem

    def selection_sort(self):
        cur = self.header
        while cur:
            _, smallestNode = self.find_smallest(cur)
            cur.key, smallestNode.key = smallestNode.key, cur.key
            cur = cur.forward
            
    def heap_sort(self):
        arr = []
        current = self.header
        while current:
            arr.append(current.key)
            current = current.forward

        heap_sorter = heapSort()
        heap_sorter.sort(arr)

        self.header = None
        for key in arr:
            self.insert_item(key)

    def merge_sort(self):
        arr = []
        current = self.header
        while current:
            arr.append(current.key)
            current = current.forward

        sorter = MergeSort()
        sorter.mergeSort(arr, 0, len(arr) - 1)

        self.header = None
        for key in arr:
            self.insert_item(key)


if __name__ == "__main__":
    # Example usage
    linked_list=LinkedListVINListManagerClass()
    linked_list.insert_item(12)
    linked_list.insert_item(19)
    linked_list.insert_item(17)
    linked_list.insert_item(26)
    linked_list.insert_item(21)
    linked_list.insert_item(3)
    linked_list.insert_item(6)
    linked_list.insert_item(7)
    linked_list.insert_item(9)
    linked_list.insert_item(25)
    linked_list.delete_item(17)

    temp=linked_list
    temp.heap_sort()
    print("Sorted list by heap_sort:")
    temp.print_items()
    
    temp=linked_list
    temp.merge_sort()
    print("Sorted list by merge_sort:")
    temp.print_items()

    print("Search for 19:", linked_list.search(19))
    print("Search for 15:", linked_list.search(15))

from skipList import skipList
from heapSort import heapSort

newList = skipList(3, 0.5)
nodeData = [76, 34, 52, 96,5, 10, 21, 30, 60,70, 80]

for data in nodeData:
    newList.insert(data)
    newList.display_list()

# Test search function
print("search for 34")
node = newList.search(34)
if node:
    print(node.key)

print("search for -1")
node = newList.search(-1)
if node:
    print(node.data)
else:
    print(node)

# Test Deletion
# Delete head
newList.delete(96)
print("Delete the head:")
newList.display_list()

# Undo delete
newList.insert(96)

# Delete the third node 34
newList.delete(34)
print("Delete the third node 34:")
newList.display_list()

newList.heap_sort()
print("Sorted list:")
newList.display_list()

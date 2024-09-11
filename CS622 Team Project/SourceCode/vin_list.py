"""
vin_list.py

As implementation scenario, vin list have been selected.
The program stores vin items for simple array, linked list, and skip list.
Each storing mechanism are separated to different files such as “simple_array_vin_list_manager.py”, “skip_list_vin_list_manager.py”, 
and "skipList.py". Each file contains FilenameClass classes with essential methods for data manipulation. 
Performance of insert/delete/lookup/selection_sort/merge_sort/heap_sort operations is measured in execution time (ms). 
"""

from simpleArray import SimpleArrayClass #type: ignore
from linkedList import LinkedListClass #type: ignore
from skipList import skipListClass

# pip install Faker for Faker installation in your computer
from faker import Faker # type: ignore 
import time
import random

item_list = [] # empty list for vin items

# We need to populate the # of items for search operation to compare between simple search and binary search
# total number of samples. Your task is to compare on those 5 values
# N = {10, 100, 1_000, 5_000, 10_000}
# Then analyze the performance between simple search and binary search
N = 10000

# Compare how search time varies depending on the position of the target location for deletion and sorting
# target_location = 0 
# target_location = N//2
# target_location = N-1 
target_location = N//2

# Parameters for a skip list
max_level = 1000    # Up to how many levels the skip list can haves
p = 0.5           # The probability that each new node has being promoted to the next level

Faker.seed(0)
fake = Faker()
# store random vin items
for i in range(0, N):
        item_list.append(fake.vin())

def main():

        target_item = item_list[target_location]   

        print("------ Simple array ------")
        sa = SimpleArrayClass()

        #insert operation
        simple_array_insert_start_time = time.perf_counter()
        for i in range(len(item_list)):
            sa.insert_item(item_list[i])
        simple_array_insert_end_time = time.perf_counter()

        # print("The current list:\t", end = " ")
        # sa.print_items()

        #search operation
        simple_array_search_start_time = time.perf_counter()
        # sa.search_item(target_item)
        simple_array_search_end_time = time.perf_counter()

        #delete operation
        simple_array_delete_start_time = time.perf_counter()
        sa.delete_item(target_item)
        simple_array_delete_end_time = time.perf_counter()
        # print("Deleted:\t", target_item, end = "\n")        
        # sa.print_items()

        #look up operation(last element)
        simple_array_lookup_start_time = time.perf_counter()
        sa_lastElement = sa.get_last_item()
        simple_array_lookup_end_time = time.perf_counter()
        # print("Look up the last element:\t%s" % sa_lastElement)
        
        #sort operation
        temp1 = sa
        simple_array_selection_sort_start_time = time.perf_counter()
        temp1.selection_sort()
        simple_array_selection_sort_end_time = time.perf_counter()
        # print("Selection-Sorted:\t", end = " ")
        # temp1.print_items()

        temp2 = sa
        simple_array_heap_sort_start_time = time.perf_counter()
        temp2.heap_sort()
        simple_array_heap_sort_end_time = time.perf_counter()
        # print("Heap-Sorted:\t", end = " ")
        # temp2.print_items()

        temp3 = sa
        simple_array_merge_sort_start_time = time.perf_counter()
        temp3.merge_sort()
        simple_array_merge_sort_end_time = time.perf_counter()
        # print("Merge-Sorted:\t", end = " ")
        # temp2.print_items()

        #time summary:
        saInsertOp = (simple_array_insert_end_time - simple_array_insert_start_time) * 1000
        saDeleteOp = (simple_array_delete_end_time - simple_array_delete_start_time) * 1000
        saLookupOp = (simple_array_lookup_end_time - simple_array_lookup_start_time) * 1000
        saSelectionSortOp= (simple_array_selection_sort_end_time - simple_array_selection_sort_start_time) * 1000
        saMergeSortOp= (simple_array_merge_sort_end_time - simple_array_merge_sort_start_time) * 1000
        saHeapSortOp= (simple_array_heap_sort_end_time - simple_array_heap_sort_start_time) * 1000
        print("Time Summary (ms):")
        print("-insertion: %.10f\n-deletion: %.10f\n-lookup: %.10f\n-selection_sort: %.10f\n-merge_sort: %.10f\n-heap_sort: %.10f\n" %(saInsertOp, saDeleteOp, saLookupOp, saSelectionSortOp, saMergeSortOp, saHeapSortOp))


        print("------ Linked list ------")
        ll = LinkedListClass()
        #insert operation
        linked_list_insert_start_time = time.perf_counter()
        for i in range(len(item_list)):
                ll.insert_item(item_list[i])
        linked_list_insert_end_time = time.perf_counter()
 
        # print("The current list:\t", end = " ")
        # ll.print_items()

        target_item = item_list[target_location]   

        #look up operation
        linked_list_lookup_start_time = time.perf_counter()
        ll_targetElement = ll.search(target_item)
        linked_list_lookup_end_time = time.perf_counter()
        # print("The look up the target element:\t%s" % ll_targetElement)
        
        #delete operation
        linked_list_delete_start_time = time.perf_counter()
        ll.delete_item(target_item)
        linked_list_delete_end_time = time.perf_counter()
        # print("Deleted:\t", target_item, end = "\n")
        # ll.print_items()
        
        #sort operation
        temp1=ll
        linked_list_selection_sort_start_time = time.perf_counter()
        temp1.selection_sort()
        linked_list_selection_sort_end_time = time.perf_counter()
        # print("Selection-Sorted:\t", end = " ")
        # temp1.print_items()

        temp2=ll
        linked_list_heap_sort_start_time = time.perf_counter()
        temp2.heap_sort()
        linked_list_heap_sort_end_time = time.perf_counter()
        # print("Heap-Sorted:\t", end = " ")
        # temp2.print_items()

        temp3 = ll
        linked_list_merge_sort_start_time = time.perf_counter()
        temp3.merge_sort()
        linked_list_merge_sort_end_time = time.perf_counter()
        # print("Merge-Sorted:\t", end = " ")
        # temp3.print_items()

        #time summary:
        llInsertOp= (linked_list_insert_end_time - linked_list_insert_start_time) * 1000
        llDeleteOp= (linked_list_delete_end_time - linked_list_delete_start_time) * 1000
        llLookupOp= (linked_list_lookup_end_time - linked_list_lookup_start_time) * 1000
        llSelectionSortOp= (linked_list_selection_sort_end_time - linked_list_selection_sort_start_time) * 1000
        llMergeSortOp= (linked_list_merge_sort_end_time - linked_list_merge_sort_start_time) * 1000
        llHeapSortOp= (linked_list_heap_sort_end_time - linked_list_heap_sort_start_time) * 1000
        print("Time Summary (ms):")
        print("-insertion: %.10f\n-deletion: %.10f\n-lookup: %.10f\n-selection_sort: %.10f\n-merge_sort: %.10f\n-heap_sort: %.10f\n" %(llInsertOp, llDeleteOp, llLookupOp, llSelectionSortOp, llMergeSortOp, llHeapSortOp))
        
        
        
        print("------ Skip list ------")
        sl = skipListClass(max_level=max_level, p=p)
        #insert operation
        skip_list_insert_start_time = time.perf_counter()
        for i in range(len(item_list)):
                sl.insert(item_list[i])
        skip_list_insert_end_time = time.perf_counter()
 
        # print("The current list:\n", end = " ")
        # sl.display_list()

        target_item = item_list[target_location]   
                
        #look up operation(last element)
        skip_list_lookup_start_time = time.perf_counter()
        sl_targetElement = sl.search(target_item)
        skip_list_lookup_end_time = time.perf_counter()
        # print("The look up the target element:\t%s" % sl_targetElement)
        
        #delete operation
        skip_list_delete_start_time = time.perf_counter()
        sl.delete(target_item)
        skip_list_delete_end_time = time.perf_counter()
        # print("Deleted:\t", target_item, end = "\n")
        # sl.display_list()
        
        #sort operation
        temp1=sl
        skip_list_selection_sort_start_time = time.perf_counter()
        temp1.selection_sort()
        skip_list_selection_sort_end_time = time.perf_counter()
        # print("Selection-Sorted:")
        # temp1.display_list()

        temp2=sl
        skip_list_heap_sort_start_time = time.perf_counter()
        temp2.heap_sort()
        skip_list_heap_sort_end_time = time.perf_counter()
        # print("Heap-Sorted:")
        # temp2.display_list()        
        
        temp3 = ll
        skip_list_merge_sort_start_time = time.perf_counter()
        temp3.merge_sort()
        skip_list_merge_sort_end_time = time.perf_counter()
        # print("Merge-Sorted:\t", end = " ")
        # temp3.print_items()

        #time summary:
        slInsertOp= (skip_list_insert_end_time - skip_list_insert_start_time) * 1000
        slDeleteOp= (skip_list_delete_end_time - skip_list_delete_start_time) * 1000
        slLookupOp= (skip_list_lookup_end_time - skip_list_lookup_start_time) * 1000
        slSelectionSortOp= (skip_list_selection_sort_end_time - skip_list_selection_sort_start_time) * 1000
        slMergeSortOp= (skip_list_merge_sort_end_time - skip_list_merge_sort_start_time) * 1000
        slHeapSortOp= (skip_list_heap_sort_end_time - skip_list_heap_sort_start_time) * 1000
        print("Time Summary (ms):")
        print("-insertion: %.10f\n-deletion: %.10f\n-lookup: %.10f\n-selection_sort: %.10f\n-merge_sort: %.10f\n-heap_sort: %.10f\n" %(slInsertOp, slDeleteOp, slLookupOp, slSelectionSortOp, slMergeSortOp, slHeapSortOp))
        

if __name__ == "__main__":
        main()

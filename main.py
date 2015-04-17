import random_generator
import sorter
import dis
import copy
import time
__author__ = 'pawel'

#def contains (array, i):

def check_sorting(array,original):
    if array == original:
        return "correct"
    else:
        return "incorrect"




def print_execution_info(array,sort_type,sort_time,original):
    print sort_type+" sort execution time: "+str(sort_time)+" Sorting: "+ check_sorting(array,original)

def test_merge_sort(array,sorter,original):
    time_start = time.clock()
    sorter.merge_sort(array)
    time_stop = time.clock()
    print_execution_info(array,"Merge",time_stop-time_start,original)

def test_bubble_sort(array,sorter,original):
    time_start = time.clock()
    sorter.bubble_sort_iteration(array)
    time_stop = time.clock()
    print_execution_info(array,"Bubble",time_stop-time_start,original)

def test_insertion_sort(array,sorter,original):
    time_start = time.clock()
    sorter.insertion_sort(array)
    time_stop = time.clock()
    print_execution_info(array,"Insertion",time_stop-time_start,original)

def test_quicksort(array,sorter,original):
    time_start = time.clock()
    sorter.quicksort(array,0,len(array)-1)
    time_stop = time.clock()
    print_execution_info(array,"Quicksort",time_stop-time_start,original)

def test_heapsort(array,sorter,original):
    time_start = time.clock()
    sorter.heapsort(array)
    time_stop = time.clock()
    print_execution_info(array,"Heapsort",time_stop-time_start,original)
def sort_with_std_function(array):
    time_start = time.clock()
    array.sort()
    time_stop = time.clock()
    print "With .sort(): "+str(time_stop-time_start)

generator = random_generator.RandomGenerator()
iterator = generator.__generate__(100,10000000)
sorter = sorter.Sorter()

original_sorted = copy.copy(iterator)
sort_with_std_function(original_sorted)

array_merge = copy.copy(iterator)
test_merge_sort(array_merge,sorter,original_sorted)

# array_bubble = copy.copy(iterator)
# test_bubble_sort(array_bubble,sorter,original_sorted)

# array_insertion = copy.copy(iterator)
# test_insertion_sort(array_insertion,sorter,original_sorted)
#
array_quick = copy.copy(iterator)
test_quicksort(array_quick,sorter,original_sorted)

array_heap = copy.copy(iterator)
test_heapsort(array_heap,sorter,original_sorted)
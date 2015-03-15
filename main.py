import random_generator
import sorter
import dis
import copy
import time
__author__ = 'pawel'

#def contains (array, i):

def check_sorting(array):
        for i in range(len(array)-1):
            if(array[i]>array[i+1]):
                return "incorrect"
        # for i in range(len(base_array)):
        #     if (!contains(base_array,array[i])):


        return "correct"

def print_execution_info(array,sort_type,sort_time):
    print sort_type+" sort execution time: "+str(sort_time)+" Sorting: "+ check_sorting(array)

def test_merge_sort(array,sorter):
    time_start = time.clock()
    sorter.merge_sort(array)
    time_stop = time.clock()
    print_execution_info(array,"Merge",time_stop-time_start)

def test_bubble_sort(array,sorter):
    time_start = time.clock()
    sorter.bubble_sort_iteration(array)
    time_stop = time.clock()
    print_execution_info(array,"Bubble",time_stop-time_start)

def test_insertion_sort(array,sorter):
    time_start = time.clock()
    sorter.insertion_sort(array)
    time_stop = time.clock()
    print_execution_info(array,"Insertion",time_stop-time_start)
generator = random_generator.RandomGenerator()
iterator = generator.__generate__(100,8)
sorter = sorter.Sorter()


array_merge = copy.copy(iterator)
test_merge_sort(array_merge,sorter)

array_bubble = copy.copy(iterator)
test_bubble_sort(array_bubble,sorter)

array_insertion = copy.copy(iterator)
test_insertion_sort(array_insertion,sorter)

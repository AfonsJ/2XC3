import good_sorts
import dual_quicksort
import timeit
import bad_sorts
import expr6toexcel
import sys


LIST_LENGTH = 2000
NUMBER_OF_RUNS = 100
INC_INDEX = 100
RECURSION_LIMIT = 3000

def set_recursion_limit(new_limit):
    sys.setrecursionlimit(new_limit)
    
def quick_sort_runtime():
    print("QUICK SORT:")
    times = []
    for current_list_length in range(INC_INDEX, LIST_LENGTH+INC_INDEX, INC_INDEX):
        total_time = 0
        random_list = bad_sorts.create_random_list(current_list_length, current_list_length)
        for _ in range(0, NUMBER_OF_RUNS):
            start =  timeit.default_timer()
            good_sorts.quicksort(random_list)#sort call
            total_time += timeit.default_timer() - start


        times.append(total_time/NUMBER_OF_RUNS)
        print ("RANDOM LIST:  SIZE:"  + str(current_list_length) + "\tTIME: " + str(total_time/NUMBER_OF_RUNS))
    expr6toexcel.quick_sort_write_to_xl(INC_INDEX, times)



def dual_quicksort_runtime():
    print("DUAL QUICK SORT:")
    times = []
    for current_list_length in range(INC_INDEX, LIST_LENGTH+INC_INDEX, INC_INDEX):
        total_time = 0
        random_list = bad_sorts.create_random_list(current_list_length, current_list_length)
        for _ in range(0, NUMBER_OF_RUNS):
            start =  timeit.default_timer()
            dual_quicksort.dual_quicksort(random_list)#sort call
            total_time += timeit.default_timer() - start


        times.append(total_time/NUMBER_OF_RUNS)
        print ("RANDOM LIST:  SIZE:"  + str(current_list_length) + "\tTIME: " + str(total_time/NUMBER_OF_RUNS))
    expr6toexcel.dual_quick_sort_write_to_xl(INC_INDEX, times)


set_recursion_limit(RECURSION_LIMIT)
quick_sort_runtime()
dual_quicksort_runtime()

from givensorts import bad_sorts
from givensorts import good_sorts
import bottom_up_merge_sort
import timeit
import expr7toexcel




LIST_LENGTH = 10000
NUMBER_OF_RUNS = 100
INC_INDEX = 500

def merge_sort_runtime():
    print("MERGE SORT:")
    times = []
    for current_list_length in range(INC_INDEX, LIST_LENGTH+INC_INDEX, INC_INDEX):
        total_time = 0
        random_list = bad_sorts.create_random_list(current_list_length, current_list_length)
        for _ in range(0, NUMBER_OF_RUNS):
            start =  timeit.default_timer()
            good_sorts.mergesort(random_list)#sort call
            total_time += timeit.default_timer() - start


        times.append(total_time/NUMBER_OF_RUNS)
        print ("RANDOM LIST:  SIZE:"  + str(current_list_length) + "\tTIME: " + str(total_time/NUMBER_OF_RUNS))
    expr7toexcel.merge_sort_write_to_xl(INC_INDEX, times)


def bottom_up_merge_sort_runtime():
    print("BOTTOM UP MERGE SORT:")
    times = []
    for current_list_length in range(INC_INDEX, LIST_LENGTH+INC_INDEX, INC_INDEX):
        total_time = 0
        random_list = bad_sorts.create_random_list(current_list_length, current_list_length)
        for _ in range(0, NUMBER_OF_RUNS):
            start =  timeit.default_timer()
            bottom_up_merge_sort.bottom_up_merge_sort(random_list)#sort call
            total_time += timeit.default_timer() - start


        times.append(total_time/NUMBER_OF_RUNS)
        print ("RANDOM LIST:  SIZE:"  + str(current_list_length) + "\tTIME: " + str(total_time/NUMBER_OF_RUNS))
    expr7toexcel.bottom_up_merge_sort_write_to_xl(INC_INDEX, times)



merge_sort_runtime()
bottom_up_merge_sort_runtime()

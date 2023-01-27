import bad_sorts
import timeit
import toexcel

LIST_LENGTH = 2000
NUMBER_OF_RUNS = 100
INC_INDEX = 100

def runtime_bubble():
    print("BUBBLE SORT")
    random_list_times = []
    near_sorted_list_times = []
    total_random = 0
    total_near_sorted = 0
    for current_list_length in range(INC_INDEX, LIST_LENGTH+INC_INDEX, INC_INDEX):
        random_list = bad_sorts.create_random_list(current_list_length, current_list_length)#(list_length, max_value)
        near_sorted = bad_sorts.create_near_sorted_list(current_list_length, current_list_length, current_list_length//(5*current_list_length))#(list_length, max_value, number_of_swaps)
        for _ in range(0, NUMBER_OF_RUNS):
            start =  timeit.default_timer()
            bad_sorts.bubble_sort(random_list)#sort call
            total_random += timeit.default_timer() - start

            start =  timeit.default_timer()
            bad_sorts.bubble_sort(near_sorted)#sort call
            total_near_sorted += timeit.default_timer() - start

        random_list_times.append(total_random/NUMBER_OF_RUNS)
        near_sorted_list_times.append(total_near_sorted/NUMBER_OF_RUNS)

        print ("RANDOM LIST:  SIZE:"  + str(current_list_length) + "\tTIME: " + str(total_random/NUMBER_OF_RUNS))
        print("NEAR SORTED:  SIZE:" + str(current_list_length) + "\tTIME: " + str(total_near_sorted/NUMBER_OF_RUNS) + "\n")
    toexcel.bubble_sort_write_to_xl(INC_INDEX, random_list_times, near_sorted_list_times)
        



def runtime_insertion():
    print("INSERTION SORT")
    random_list_times = []
    near_sorted_list_times = []
    total_random = 0
    total_near_sorted = 0
    for current_list_length in range(INC_INDEX, LIST_LENGTH+INC_INDEX, INC_INDEX):
        random_list = bad_sorts.create_random_list(current_list_length, current_list_length)#(list_length, max_value)
        near_sorted = bad_sorts.create_near_sorted_list(current_list_length, current_list_length, current_list_length//(5*current_list_length))#(list_length, max_value, number_of_swaps)
        for _ in range(0, NUMBER_OF_RUNS):
            start =  timeit.default_timer()
            bad_sorts.bubble_sort(random_list)#sort call
            total_random += timeit.default_timer() - start

            start =  timeit.default_timer()
            bad_sorts.bubble_sort(near_sorted)#sort call
            total_near_sorted += timeit.default_timer() - start

        random_list_times.append(total_random/NUMBER_OF_RUNS)
        near_sorted_list_times.append(total_near_sorted/NUMBER_OF_RUNS)

        print ("RANDOM LIST:  SIZE:"  + str(current_list_length) + "\tTIME: " + str(total_random/NUMBER_OF_RUNS))
        print("NEAR SORTED:  SIZE:" + str(current_list_length) + "\tTIME: " + str(total_near_sorted/NUMBER_OF_RUNS) + "\n")
    toexcel.insertion_sort_write_to_xl(INC_INDEX, random_list_times, near_sorted_list_times)


def runtime_selection():
    print("SELECTION SORT")
    random_list_times = []
    near_sorted_list_times = []
    total_random = 0
    total_near_sorted = 0
    for current_list_length in range(INC_INDEX, LIST_LENGTH+INC_INDEX, INC_INDEX):
        random_list = bad_sorts.create_random_list(current_list_length, current_list_length)#(list_length, max_value)
        near_sorted = bad_sorts.create_near_sorted_list(current_list_length, current_list_length, current_list_length//(5*current_list_length))#(list_length, max_value, number_of_swaps)
        for _ in range(0, NUMBER_OF_RUNS):
            start =  timeit.default_timer()
            bad_sorts.bubble_sort(random_list)#sort call
            total_random += timeit.default_timer() - start

            start =  timeit.default_timer()
            bad_sorts.bubble_sort(near_sorted)#sort call
            total_near_sorted += timeit.default_timer() - start

        random_list_times.append(total_random/NUMBER_OF_RUNS)
        near_sorted_list_times.append(total_near_sorted/NUMBER_OF_RUNS)

        print ("RANDOM LIST:  SIZE:"  + str(current_list_length) + "\tTIME: " + str(total_random/NUMBER_OF_RUNS))
        print("NEAR SORTED:  SIZE:" + str(current_list_length) + "\tTIME: " + str(total_near_sorted/NUMBER_OF_RUNS) + "\n")
    toexcel.selection_sort_write_to_xl(INC_INDEX, random_list_times, near_sorted_list_times)



runtime_bubble()
runtime_insertion()
runtime_selection()
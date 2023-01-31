import bad_sorts
import timeit
import expr1toexcel

LIST_LENGTH = 2000
NUMBER_OF_RUNS = 100
INC_INDEX = 100

def runtime_bubble():
    print("BUBBLE SORT")
    random_list_times = []
    
    for current_list_length in range(INC_INDEX, LIST_LENGTH+INC_INDEX, INC_INDEX):
        total_random = 0
        random_list = bad_sorts.create_random_list(current_list_length, current_list_length)#(list_length, max_value)
        for _ in range(0, NUMBER_OF_RUNS):
            start_random =  timeit.default_timer()
            bad_sorts.bubble_sort(random_list)#sort call
            total_random += timeit.default_timer() - start_random


        random_list_times.append(total_random/NUMBER_OF_RUNS)

        print ("RANDOM LIST:  SIZE:"  + str(current_list_length) + "\tTIME: " + str(total_random/NUMBER_OF_RUNS))
    expr1toexcel.bubble_sort_write_to_xl(INC_INDEX, random_list_times)
        



def runtime_insertion():
    print("INSERTION SORT")
    random_list_times = []
    
    for current_list_length in range(INC_INDEX, LIST_LENGTH+INC_INDEX, INC_INDEX):
        total_random = 0
        random_list = bad_sorts.create_random_list(current_list_length, current_list_length)#(list_length, max_value)
        for _ in range(0, NUMBER_OF_RUNS):
            start_random =  timeit.default_timer()
            bad_sorts.insertion_sort(random_list)#sort call
            total_random += timeit.default_timer() - start_random


        random_list_times.append(total_random/NUMBER_OF_RUNS)

        print ("RANDOM LIST:  SIZE:"  + str(current_list_length) + "\tTIME: " + str(total_random/NUMBER_OF_RUNS))
    expr1toexcel.insertion_sort_write_to_xl(INC_INDEX, random_list_times)


def runtime_selection():
    print("SELECTION SORT")
    random_list_times = []
    for current_list_length in range(INC_INDEX, LIST_LENGTH+INC_INDEX, INC_INDEX):
        total_random = 0
        random_list = bad_sorts.create_random_list(current_list_length, current_list_length)#(list_length, max_value)
        for _ in range(0, NUMBER_OF_RUNS):
            start_random =  timeit.default_timer()
            bad_sorts.selection_sort(random_list)#sort call
            total_random += timeit.default_timer() - start_random


        random_list_times.append(total_random/NUMBER_OF_RUNS)

        print ("RANDOM LIST:  SIZE:"  + str(current_list_length) + "\tTIME: " + str(total_random/NUMBER_OF_RUNS))
    expr1toexcel.selection_sort_write_to_xl(INC_INDEX, random_list_times)



runtime_bubble()
runtime_insertion()
runtime_selection()
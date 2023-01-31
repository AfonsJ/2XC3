import bad_sorts
import timeit
import exp3toexcel

LIST_LENGTH = 5000##5000
NUMBER_OF_RUNS = 100##100
INC_INDEX = 250#250

#We are running the experiment where we will compare the 3 bad sorting algorithms runtime vs number of swaps made
#i.e... For a fixed list of 5000 elements
#   number of swaps|time taken
#   100            |time taken for a list of 100 random swaps
#   200            |time taken for a list of 200 random swaps
#   300            |time taken for a list of 300 random swaps
#etc...

def runtime_bubble():
    print("BUBBLE SORT")
    near_sorted_list_times = []
    
    for current_list_length in range(INC_INDEX, LIST_LENGTH+INC_INDEX, INC_INDEX):
        total_near_sorted = 0
        near_sorted = bad_sorts.create_near_sorted_list(current_list_length, current_list_length, current_list_length)#(list_length, max_value, number_of_swaps)
        for _ in range(0, NUMBER_OF_RUNS):

            start_near_sorted =  timeit.default_timer()
            bad_sorts.bubble_sort(near_sorted)#sort call
            total_near_sorted += timeit.default_timer() - start_near_sorted

        near_sorted_list_times.append(total_near_sorted/NUMBER_OF_RUNS)

        print("NEAR SORTED:  #OFSWAPS:" + str(current_list_length) + "\tTIME: " + str(total_near_sorted/NUMBER_OF_RUNS) + "\n")
    exp3toexcel.bubble_sort_write_to_xl(INC_INDEX, near_sorted_list_times)
        



def runtime_insertion():
    print("INSERTION SORT")
    near_sorted_list_times = []
    
    for current_list_length in range(INC_INDEX, LIST_LENGTH+INC_INDEX, INC_INDEX):
        total_near_sorted = 0
        near_sorted = bad_sorts.create_near_sorted_list(current_list_length, current_list_length, current_list_length)#(list_length, max_value, number_of_swaps)
        for _ in range(0, NUMBER_OF_RUNS):

            start_near_sorted =  timeit.default_timer()
            bad_sorts.insertion_sort(near_sorted)#sort call
            total_near_sorted += timeit.default_timer() - start_near_sorted

        near_sorted_list_times.append(total_near_sorted/NUMBER_OF_RUNS)

        print("NEAR SORTED:  #OFSWAPS:" + str(current_list_length) + "\tTIME: " + str(total_near_sorted/NUMBER_OF_RUNS) + "\n")
    exp3toexcel.insertion_sort_write_to_xl(INC_INDEX, near_sorted_list_times)


def runtime_selection():
    print("SELECTION SORT")
    near_sorted_list_times = []
    
    for current_list_length in range(INC_INDEX, LIST_LENGTH+INC_INDEX, INC_INDEX):
        total_near_sorted = 0
        near_sorted = bad_sorts.create_near_sorted_list(current_list_length, current_list_length, current_list_length)#(list_length, max_value, number_of_swaps)
        for _ in range(0, NUMBER_OF_RUNS):

            start_near_sorted =  timeit.default_timer()
            bad_sorts.selection_sort(near_sorted)#sort call
            total_near_sorted += timeit.default_timer() - start_near_sorted

        near_sorted_list_times.append(total_near_sorted/NUMBER_OF_RUNS)

        print("NEAR SORTED:  #OFSWAPS:" + str(current_list_length) + "\tTIME: " + str(total_near_sorted/NUMBER_OF_RUNS) + "\n")
    exp3toexcel.selection_sort_write_to_xl(INC_INDEX, near_sorted_list_times)



runtime_bubble()
runtime_insertion()
runtime_selection()
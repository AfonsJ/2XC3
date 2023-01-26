import bad_sorts
import timeit
# import matplotlib.pyplot as plot

LIST_LENGTH = 2000
NUMBER_OF_RUNS = 100

def runtime_bubble():
    print("BUBBLE SORT")
    total_random = 0
    total_near_sorted = 0
    for _ in range(0, LIST_LENGTH, 50):
        random_list = bad_sorts.create_random_list(LIST_LENGTH, LIST_LENGTH)#(list_length, max_value)
        near_sorted = bad_sorts.create_near_sorted_list(LIST_LENGTH, LIST_LENGTH, LIST_LENGTH//(5*LIST_LENGTH))#(list_length, max_value, number_of_swaps)

        start =  timeit.default_timer()
        bad_sorts.bubble_sort(random_list)#sort call
        total_random += timeit.default_timer() - start

        start =  timeit.default_timer()
        bad_sorts.bubble_sort(near_sorted)#sort call
        total_near_sorted += timeit.default_timer() - start

    print ("RANDOM LIST: " + str(total_random/NUMBER_OF_RUNS))
    print("NEAR SORTED: " + str(total_near_sorted/NUMBER_OF_RUNS) + "\n")
        



def runtime_insertion():
    print("INSERTION SORT")
    total_random = 0
    total_near_sorted = 0
    for _ in range(NUMBER_OF_RUNS):
        random_list = bad_sorts.create_random_list(LIST_LENGTH, LIST_LENGTH)#(list_length, max_value)
        near_sorted = bad_sorts.create_near_sorted_list(LIST_LENGTH, LIST_LENGTH, LIST_LENGTH//(5*LIST_LENGTH))#(list_length, max_value, number_of_swaps)

        start =  timeit.default_timer()
        bad_sorts.insertion_sort(random_list)#sort call
        total_random += timeit.default_timer() - start

        start =  timeit.default_timer()
        bad_sorts.insertion_sort(near_sorted)#sort call
        total_near_sorted += timeit.default_timer() - start

    print ("RANDOM LIST: " + str(total_random/NUMBER_OF_RUNS))
    print("NEAR SORTED: " + str(total_near_sorted/NUMBER_OF_RUNS)+ "\n")


def runtime_selection():
    print("SELECTION SORT")
    total_random = 0
    total_near_sorted = 0
    for _ in range(NUMBER_OF_RUNS):
        random_list = bad_sorts.create_random_list(LIST_LENGTH, LIST_LENGTH)#(list_length, max_value)
        near_sorted = bad_sorts.create_near_sorted_list(LIST_LENGTH, LIST_LENGTH, LIST_LENGTH//(5*LIST_LENGTH))#(list_length, max_value, number_of_swaps)

        start =  timeit.default_timer()
        bad_sorts.selection_sort(random_list)#sort call
        total_random += timeit.default_timer() - start

        start =  timeit.default_timer()
        bad_sorts.selection_sort(near_sorted)#sort call
        total_near_sorted += timeit.default_timer() - start

    print ("RANDOM LIST: " + str(total_random/NUMBER_OF_RUNS))
    print("NEAR SORTED: " + str(total_near_sorted/NUMBER_OF_RUNS)+ "\n")


print("LENGTH: " + str(LIST_LENGTH))
print("NUMBER OF RUNS: " + str(NUMBER_OF_RUNS)+ "\n")
runtime_bubble()
runtime_insertion()
runtime_selection()
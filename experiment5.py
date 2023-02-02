import bad_sorts
import good_sorts
import timeit


alldata = []
# number of runs
for t in range(100):
    arr = []
    # number of swaps (swap 30 times)
    for i in range(10,):
        #list max size 1000, largest num 500
        l = bad_sorts.create_near_sorted_list(1000, 500, i)

        start = timeit.default_timer()
        good_sorts.quicksort(l)
        total = timeit.default_timer() - start
        arr.append(total)
    
    alldata.append(arr)

print(len(alldata))


import bad_sorts
import good_sorts
import timeit


alldata = []
finalresults = []
# number of runs
for t in range(100):
    arr = []
    # number of swaps (swap 30 times)
    for i in range(10,301,10):
        #list max size 800, largest num 500
        l = bad_sorts.create_near_sorted_list(800, 500, i)

        start = timeit.default_timer()
        good_sorts.quicksort(l)
        total = timeit.default_timer() - start
        arr.append(total)
    
    alldata.append(arr)

print(len(alldata))


# from the 100 runs, get an average for each swap amount
for m in range(len(alldata[0])):
    subt = 0
    for result in alldata:
        subt += result[m]


    finalresults.append(subt/len(alldata))

g=10
for i in finalresults:
    print('Average time for '+str(g)+' swaps: '+ str(i))
    g += 10


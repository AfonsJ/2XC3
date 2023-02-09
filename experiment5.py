import bad_sorts
import good_sorts
import timeit
import expr5toexcel

alldataqs = []
alldatahs = []
alldatams = []

for i in range(10, 301, 10):
    avgqs = 0
    avgms = 0
    avghs = 0
    for j in range(100):
        l = bad_sorts.create_near_sorted_list(1000, 500, i)

        start = timeit.default_timer()
        good_sorts.quicksort(l)
        total = timeit.default_timer() - start

        start = timeit.default_timer()
        good_sorts.heapsort(l)
        totalh = timeit.default_timer() - start

        start = timeit.default_timer()
        good_sorts.mergesort(l)
        totalm = timeit.default_timer() - start

        avgqs += total
        avgms += totalm
        avghs += totalh

    alldataqs.append(avgqs/100.0)
    alldatams.append(avgms/100.0)
    alldatahs.append(avghs/100.0)

expr5toexcel.quick_sort_write_to_xl(10,alldataqs)
expr5toexcel.merge_sort_write_to_xl(10,alldatams)
expr5toexcel.heap_sort_write_to_xl(10,alldatahs)



# number of runs
# for t in range(100):
#     arr = []
#     arrh = []
#     arrm = []
#     # number of swaps (swap 30 times)
#     for i in range(10,301,10):
#         #list max size 800, largest num 500
#         l = bad_sorts.create_near_sorted_list(800, 500, i)

#         start = timeit.default_timer()
#         good_sorts.quicksort(l)
#         total = timeit.default_timer() - start

#         start = timeit.default_timer()
#         good_sorts.heapsort(l)
#         totalh = timeit.default_timer() - start

#         start = timeit.default_timer()
#         good_sorts.mergesort(l)
#         totalm = timeit.default_timer() - start

#         arr.append(total)
#         arrh.append(totalh)
#         arrm.append(totalm)

#     alldataqs.append(arr)
#     alldatahs.append(arrh)
#     alldatams.append(arrm)



# def getAvgForSwaps(list):
#     for m in range(len(list[0])):
#         subt = 0
#         for result in list:
#             subt += result[m]

#         return subt/len(alldataqs)




# for i in range(len(alldataqs)):
#     finalresultqs.append(getAvgForSwaps(alldataqs[i]))
#     finalresultms.append(getAvgForSwaps(alldatams[i]))
#     finalresulths.append(getAvgForSwaps(alldatahs[i]))

# from the 100 runs, get an average for each swap amount
# for m in range(len(alldataqs[0])):
#     subt = 0
#     for result in alldataqs:
#         subt += result[m]


#     finalresultqs.append(subt/len(alldataqs))
 

# g=10
# for i in range(len(finalresultqs)):
#     print('Average time for '+str(g)+' QS swaps: '+ str(finalresultqs[i]))
#     print('Average time for '+str(g)+' MS swaps: '+ str(finalresultms[i]))
#     print('Average time for '+str(g)+' HS swaps: '+ str(finalresulths[i]))
#     g += 10

# for i in range(len(finalresultqs)):
#     expr5toexcel.quick_sort_write_to_xl(10,finalresultqs)
#     expr5toexcel.merge_sort_write_to_xl(10,finalresultms)
#     expr5toexcel.heap_sort_write_to_xl(10,finalresulths)
from givensorts import bad_sorts
from givensorts import good_sorts
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


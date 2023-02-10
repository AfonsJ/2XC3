import random
import time
import timeit
import matplotlib.pyplot as plot
# import numpy as np



# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


# Creates a near sorted list by creating a random list, sorting it, then doing a random number of swaps
def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L

def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

def insertion_sort(L):
    for i in range(1, len(L)):
        insert(L, i)


def insert(L, i):
    while i > 0:
        if L[i] < L[i-1]:
            swap(L, i-1, i)
            i -= 1
        else:
            return

def quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)

# *************************************


# ************ Merge Sort *************

def mergesort(L):
    if len(L) <= 1:
        return
    mid = len(L) // 2
    left, right = L[:mid], L[mid:]

    mergesort(left)
    mergesort(right)
    temp = merge(left, right)

    for i in range(len(temp)):
        L[i] = temp[i]


def merge(left, right):
    L = []
    i = j = 0

    while i < len(left) or j < len(right):
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[j])
                j += 1
    return L

def measure_time(sort_func, array):
    start = timeit.default_timer()
    sort_func(array)
    end = timeit.default_timer()
    return end - start

num_runs = 100

insertion_sort_times = []
merge_sort_times = []
quick_sort_times = []

for length in range(0, 50, 1):
    heap_sort_time = 0
    merge_sort_time = 0
    quick_sort_time = 0
    for _ in range(num_runs):
        array = create_random_list(length, length)
        heap_sort_time += measure_time(insertion_sort, array[:])
        merge_sort_time += measure_time(mergesort, array[:])
        quick_sort_time += measure_time(quicksort, array[:])
    insertion_sort_times.append(heap_sort_time / num_runs)
    merge_sort_times.append(merge_sort_time / num_runs)
    quick_sort_times.append(quick_sort_time / num_runs)

plot.plot(range(0, 50, 1), insertion_sort_times, label='Insertion Sort')
plot.plot(range(0, 50, 1), merge_sort_times, label='Merge Sort')
plot.plot(range(0, 50, 1), quick_sort_times, label='Quick Sort')

plot.xlabel('List Length')
plot.ylabel('Time (seconds)')
plot.title('Comparison of Sorting Algorithms')
plot.legend()
plot.show()
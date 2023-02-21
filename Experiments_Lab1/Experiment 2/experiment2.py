import random
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

# I have created this function to make the sorting algorithm code read easier
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

# Original selection sort function
def selection_sort(L):
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)


def find_min_index(L, n):
    min_index = n
    for i in range(n+1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index

def find_max_index(L, n):
    max_index = n
    for i in range(n+1, len(L)):
        if L[i] > L[max_index]:
            max_index = i
    return max_index

# Improved selection sort function
def selection_sort2(L):
    for i in range(len(L) - 1):
        min_index = i
        max_index = i
        for j in range(i + 1, len(L)):
            if L[j] < L[min_index]:
                min_index = j
            if L[j] > L[max_index]:
                max_index = j
        swap(L, i, min_index)
        swap(L, len(L)-1, max_index)
    return L

#regular bubblesort
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)
    return L

#improved bubblesort
def bubble_sort2(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                value = L[j]
                L[j] = L[j+1]
                insert_value(L, value, j+1)
    return L
                
def insert_value(L, value, i):
    while i < len(L) - 1 and value > L[i]:
        L[i] = L[i+1]
        i += 1
    L[i] = value

# Function to measure running time of Insertion sort
def measure_time(arr):
    start = timeit.default_timer()
    bubble_sort2(arr)
    end = timeit.default_timer()
    return end - start

# Number of runs
runs = 100

# Create list to store the running times
times = []

# Loop through different list lengths
for length in range(100, 1000, 100):
    total_time = 0
    for run in range(runs):
        # Create a random list of the current length
        arr = create_random_list(length, length)
        total_time += measure_time(arr)
    average_time = total_time / runs
    times.append(average_time)

# Plot the results
plot.plot(range(1000, 10000, 1000), times)
plot.xlabel('List length')
plot.ylabel('Running time (seconds)')
plot.title('Bubble_sort2')
plot.show()

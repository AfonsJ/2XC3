def dual_quicksort(L):
    copy = dual_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def dual_quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot_1 = L[0]
    pivot_2 = L[1]
    left, right, middle = [], [], []
    for num in L[2:]:
        if num < pivot_1 and num < pivot_2:
            left.append(num)
        elif num > pivot_1 and num > pivot_2:
            right.append(num)
        else:
            middle.append(num)
            
    return dual_quicksort_copy(left) + [pivot_1] + dual_quicksort_copy(middle) + [pivot_2] + dual_quicksort_copy(right)



    
# L = [3,7,5,0,1,8,2,6,9,4]
# dual_quicksort(L)
# print(L)
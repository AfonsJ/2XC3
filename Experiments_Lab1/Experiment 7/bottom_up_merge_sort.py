def bottom_up_merge_sort(arr):
    length = len(arr)
    chunk_size = 1
    while chunk_size < length:
        for start in range(0, length, 2 * chunk_size):
            arr[start:start + 2 * chunk_size] = merge(arr[start:start + chunk_size], arr[start + chunk_size:start + 2 * chunk_size])
        chunk_size *= 2
    return arr

def merge(left_arr, right_arr):
    result = []
    i = j = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1
    result += left_arr[i:]
    result += right_arr[j:]
    return result



# # L = [3,7,5,0,1,8,2,6,9,4]
# L = []
# for i in range(1000, 0, -1):
#     L. append(i)
# print(L)
# print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

# bottom_up_merge_sort(L)
# print(L)

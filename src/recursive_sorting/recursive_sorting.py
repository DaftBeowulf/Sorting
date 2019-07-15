# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []
    # TO-DO
    i = 0
    j = 0

    while arrA[i:] and arrB[j:]:
        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        else:
            merged_arr.append(arrB[j])
            j += 1
    if not arrA[i:]:
        merged_arr.extend(arrB[j:])
    else:
        merged_arr.extend(arrA[i:])

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # find pivot (half-way point)
    pivot = int(len(arr)/2)

    if len(arr) > 2:
        # split arr, pass recursively until both halves have come back and are sorted (in elif statement)
        lhs = merge_sort(arr[:pivot])
        rhs = merge_sort(arr[pivot:])
        # then merge both sorted halves
        arr = merge(lhs, rhs)
    elif len(arr) == 2:
        # if only two items, just pass in to merge so they get sorted properly
        arr = merge(arr[:pivot], arr[pivot:])

    # if arr of only ONE item is passed here, it just gets returned
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr

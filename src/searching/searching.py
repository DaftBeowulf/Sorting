# STRETCH: implement Linear Search
def linear_search(arr, target):
    # for i in range(len(arr)):
    #     if arr[i] == target:
    #         return arr[i]
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    # TO-DO: add missing code

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    elif arr[middle] == target:
                # middle is target: success!
        return middle
    elif arr[middle] > target:
                # target is to the left
        return binary_search_recursive(arr[:middle], target, low, middle)
    else:
                # target is to the right
        return binary_search_recursive(arr[middle:], target, middle, high)

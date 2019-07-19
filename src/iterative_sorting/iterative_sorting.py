# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=200):
    result = [0]*len(arr)
    keys = [0]*maximum

    for i in arr:
        if i < 0:
            return 'Error, negative numbers not allowed in Count Sort'
        keys[i] += 1

    # previous version, I tried to get too fancy by comparing the key with the next key
    # for i, item in enumerate(keys):
    #     if i != 0:
    #         keys[i] += keys[i-1]
    # keys = [0]+keys[:len(keys)-1]

    x = 0
    for i in range(len(keys)):
        while keys[i] > 0:
            result[x] = i
            x += 1
            keys[i] -= 1

    return result


arr1 = [0, 3, 8, 1, 2, 9, 6, 4, 5, 7]
print(count_sort(arr1))

# pseudocode
# function countingSort(array, k) is
#   count ← new array of k zeros
#   for i = 1 to length(array) do`
#     count[array[i]] ← count[array[i]] + 1
#   for i = 2 to k do
#     count[i] ← count[i] + count[i - 1]
#   for i = length(array) downto 1 do
#     output[count[array[i]]] ← array[i]
#     count[array[i]] ← count[array[i]] - 1
#   return output

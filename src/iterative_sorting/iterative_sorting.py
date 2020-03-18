# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # print(arr) <- used for testing
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for _ in range(len(arr) - i):
            if arr[cur_index] < arr[smallest_index]:
               smallest_index = cur_index
            cur_index += 1

        # TO-DO: swap
        cur_value = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = cur_value



    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # Iterate from first to last, 'swapping' pairs if the earlier is larger than the later
    if len(arr) <= 1:
        return arr
    no_swap = 0
    while True:
        # print(arr) <- used for testing
        # Start at index 0 and index 1
        for i in range(len(arr)):
            earlier_index = i
            later_index = i + 1
            if earlier_index == len(arr) - 1:
                break
            # save values to prevent loss
            earlier_value = arr[earlier_index]
            later_value = arr[later_index]
            # is index 0 bigger than 1?
            # Yes: swap 0 and 1
            if earlier_value >= later_value:
                arr[earlier_index] = later_value
                arr[later_index] = earlier_value
            # No: leave as is
            else:
                no_swap += 1
        if no_swap == len(arr) - 1:
            break
        no_swap = 0
    # move to index 1 and 2 and loop until last index is used
    # stop when no swaps happen
    return arr

# Used for testing
# test_array = [6, 2, 1, 3]
# print(bubble_sort(test_array))
# print(selection_sort(test_array))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
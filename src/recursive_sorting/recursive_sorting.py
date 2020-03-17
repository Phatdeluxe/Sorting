# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # TO-DO
    merged_arr = []
    a = arrA
    b = arrB

    while len(a) > 0 and len(b) > 0:
        if a[0] > b[0]:
            merged_arr.append(b[0])
            b.pop(0)
        else:
            merged_arr.append(a[0])
            a.pop(0)
    
    while len(a) > 0:
        merged_arr.append(a[0])
        a.pop(0)

    while len(b) > 0:
        merged_arr.append(b[0])
        b.pop(0)

    return merged_arr

# test1 = [1, 5, 6]
# test2 = [2, 3, 4, 10, 11]
# print(merge(test1, test2))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) == 0:
        return arr
    if len(arr) == 1:
        return arr
    
    temp_arr1 = [] 
    temp_arr2 = []
    for i in range(0, len(arr) // 2):
        temp_arr1.append(arr[i])
    for i in range((len(arr) // 2), len(arr)):
        temp_arr2.append(arr[i])

    temp_arr1 = merge_sort(temp_arr1)
    temp_arr2 = merge_sort(temp_arr2)

    return merge(temp_arr1, temp_arr2)

# test_arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print(merge_sort(test_arr))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

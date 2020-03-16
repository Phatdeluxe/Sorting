# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  for i in range(len(arr)):
    if arr[i] == target:
      return i

  return -1   # not found

test_array = [1, 2, 3, 4, 5, 6, 7]
print(linear_search(test_array, 8))


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  found = -1
  while low <= high and found == -1:
    middle = (low + high) // 2
    if arr[middle] == target:
      found = middle

    else:
      if arr[middle] > target:
        high = middle - 1
      else:
        low = middle + 1

  return found # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls

def linear_search(arr, target):
    # Your code here
    for i in range (0, len(arr)):
        if target == arr[i]:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = round((l + r) / 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1


    return -1  # not found



arr = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
print(binary_search(arr,6))
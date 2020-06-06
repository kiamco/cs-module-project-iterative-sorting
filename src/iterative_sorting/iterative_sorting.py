# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here

        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp
        print(arr, smallest_index, cur_index)

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    print(arr)
    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    max_num = None if maximum is None else maximum

    # find max if maximum is none
    if maximum is None:
        max_num = arr[0]
        for i in range(0, len(arr)):
            if max_num < arr[i]:
                max_num = arr[i]


    # create count arr
    count_arr = [0] * (max_num + 1)

    for i in range(0, len(arr) ):
        count_arr[arr[i]] += 1

    # transform count arr
    for j in range(1, len(count_arr) ):
        count_arr[j] = count_arr[j] + count_arr[j - 1]
    
    newArr = [0] * len(arr)

    for k in reversed(range(0, len(arr))):
        count_pointer = len(count_arr) - 1 
        count_arr[count_pointer] -= 1
        count_pointer = count_pointer - 1
        print(count_pointer)

        # newArr[count_arr[k]] = arr[k]

    print(newArr)
    # create new arr

    # print(count_arr)
    return arr



arr = [2,5,3,4,1,6,7,7,7,2,2]
counting_sort(arr)
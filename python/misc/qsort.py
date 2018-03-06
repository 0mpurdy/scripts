# Quicksort implemented in a couple of different ways
# also includes some timing

import random
import timeit

# not in place, uses extend
def qsort1(numbers):
    if (len(numbers) == 0):
        return []
    if (len(numbers) == 1):
        return numbers
    smaller = []
    larger = []
    pivot = numbers[0]
    for number in numbers[1:]:
        if (number > pivot):
            larger.append(number)
        else:
            smaller.append(number)
    result = qsort(smaller)
    result.append(pivot)
    result.extend(qsort(larger))
    return result

# not in place
def qsort2(arr):
    if (len(arr) <= 1):
        return arr
    
    smaller = []
    larger = []
    equal = []

    #print("pivot %d" % ((len(numbers) + 1)//2))
    pivot = arr[(len(arr) + 1)//2]
    for item in arr:
        if (item > pivot):
            larger.append(item)
        elif (item < pivot):
            smaller.append(item)
        else:
            equal.append(item)
    return qsort(smaller) + equal + qsort(larger)

# adapted from https://stackoverflow.com/questions/18262306/quicksort-with-python
def partition(arr, begin, end):
    pivot = begin
    for i in range(begin + 1, end + 1):
        if (arr[i] <= arr[begin]):
            pivot += 1
            arr[i], arr[pivot] = arr[pivot], arr[i]
    arr[pivot], arr[begin] = arr[begin], arr[pivot]
    #print(begin, end, pivot, ":", arr[begin], "\n\t", arr)
    return pivot

def qsort(arr, begin = 0, end = None):
    if (end is None):
        end = len(arr) - 1
    # inner so that end is None only checked once
    def iqsort(arr, begin, end):
        if (begin >= end):
            return
        pivot = partition(arr, begin, end)
        iqsort(arr, begin, pivot-1)
        iqsort(arr, pivot+1, end)
        return arr
    return iqsort(arr, begin, end)

# time creation of random numbers
time = timeit.timeit('[int(1000*random.random()) for i in range(10000)]', setup = 'import random', number = 100)
print('Random time:', time)

#initial = [2,4,1,2,7,5,2,7,2,58,7,9,3,976,5,2,35,3,6,2,34]
initial = [int(1000*random.random()) for i in range(1000)]

def qwrapper():
    initial = [int(10000*random.random()) for i in range(1000)]
    finished = qsort(initial)
    #print(finished)

time = timeit.timeit(qwrapper, number = 1000)
print('Sort time:', time)

finished = qsort(initial)
print('Done')
    

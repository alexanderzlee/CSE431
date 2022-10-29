# REFERENCES
# https://www.geeksforgeeks.org/visualization-of-merge-sort-using-matplotlib/
# https://www.geeksforgeeks.org/insertion-sort-visualization-using-matplotlib-in-python/
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import axes3d
import matplotlib as mp
import numpy as np
import random
import timeit
import time

# insertion sort algorithm
def insertionsort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1

        while (i >= 0 and a[i] > key):
            a[i + 1] = a[i]
            i -= 1
            yield a
        a[i + 1] = key

        yield a


# function to recursively divide the array
def mergesort(A, start, end):
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1

    # yield from statements have been used to yield
    # the array from the functions
    yield from mergesort(A, start, mid)
    yield from mergesort(A, mid + 1, end)
    yield from merge(A, start, mid, end)


# function to merge the array
def merge(A, start, mid, end):
    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if A[leftIdx] < A[rightIdx]:
            merged.append(A[leftIdx])
            leftIdx += 1
        else:
            merged.append(A[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(A[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(A[rightIdx])
        rightIdx += 1

    for i in range(len(merged)):
        A[start + i] = merged[i]
        yield A


# function to recursively divide the array
def timsort(A, start, end, k):
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1

    if (end - start) <= k:
        insertionsort(A)
    else:
        # yield from statements have been used to yield
        # the array from the functions
        yield from timsort(A, start, mid, k)
        yield from timsort(A, mid + 1, end, k)
        yield from merge(A, start, mid, end)


SETUP_CODE = '''
from __main__ import mergesort
from __main__ import insertionsort
from __main__ import timsort
import random
random.seed(0)
'''

MERGE_TEST_CODE = '''
n = 1500
a = [i for i in range(1, n + 1)]
random.shuffle(a)
mergesort(a, 0, len(a) - 1)'''

INSERTION_TEST_CODE = '''
n = 1500
a = [i for i in range(1, n + 1)]
random.shuffle(a)
insertionsort(a)'''

TIM_TEST_CODE = '''
n = 1500
a = [i for i in range(1, n + 1)]
random.shuffle(a)
timsort(a, 0, len(a) - 1, 15)'''

mergetime = timeit.timeit(setup=SETUP_CODE, stmt=MERGE_TEST_CODE, number=1000)
print('merge sort time: {}'.format(mergetime))
insertiontime = timeit.timeit(setup=SETUP_CODE, stmt=INSERTION_TEST_CODE, number=1000)
print('insertion sort time: {}'.format(insertiontime))
timtime = timeit.timeit(setup=SETUP_CODE, stmt=TIM_TEST_CODE, number=1000)
print('tim sort time: {}'.format(timtime))

k = 50
n = 3000
plt.ylabel('Runtime (seconds)')
plt.xlabel('k value')

times = [0]
values = [1]
times_insertion = [0]
tim_times = [0]
for i in range(1, k):
    values.append(i)

    # merge
    start = timeit.default_timer()
    a = [j for j in range(1, n + 1)]
    random.shuffle(a)
    mergesort(a, 0, len(a) - 1)
    end = timeit.default_timer()
    times.append(end - start)

    # insertion
    start_insertion = timeit.default_timer()
    a = [j for j in range(1, n + 1)]
    random.shuffle(a)
    insertionsort(a)
    end_insertion = timeit.default_timer()
    times_insertion.append(end_insertion - start_insertion)

    # tim
    start = timeit.default_timer()
    a = [j for j in range(1, n + 1)]
    random.shuffle(a)
    timsort(a, 0, len(a) - 1, i)
    end = timeit.default_timer()
    tim_times.append(end - start)

plt.plot(values, times, label="merge sort")
plt.plot(values, times_insertion, label="insertion sort")
plt.plot(values, tim_times, label="tim sort")

plt.grid()
plt.legend()
plt.show()

# REFERENCES
# https://www.geeksforgeeks.org/visualization-of-merge-sort-using-matplotlib/
# https://www.geeksforgeeks.org/insertion-sort-visualization-using-matplotlib-in-python/
import matplotlib.pyplot as plt
import random
import timeit


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


SETUP_CODE = '''
from __main__ import mergesort
from __main__ import insertionsort
'''

MERGE_TEST_CODE = '''
import random
n = 1500
a = [i for i in range(1, n + 1)]
random.shuffle(a)
mergesort(a, 0, len(a) - 1)'''

INSERTION_TEST_CODE = '''
import random
n = 1500
a = [i for i in range(1, n + 1)]
random.shuffle(a)
insertionsort(a)'''

mergetime = timeit.timeit(setup=SETUP_CODE, stmt=MERGE_TEST_CODE, number=1000)
print('merge sort time: {}'.format(mergetime))
insertiontime = timeit.timeit(setup=SETUP_CODE, stmt=INSERTION_TEST_CODE, number=1000)
print('insertion sort time: {}'.format(insertiontime))
print('merge/insertion ratio:', mergetime/insertiontime)

n = 3000

plt.ylabel('Runtime (seconds)')
plt.xlabel('Number of elements (n)')

times = [0]
values = [1]
times_insertion = [0]
for i in range(1, n):
    values.append(i)

    #merge
    start = timeit.default_timer()
    a = [j for j in range(1, i + 1)]
    random.shuffle(a)
    mergesort(a, 0, len(a) - 1)
    end = timeit.default_timer()
    times.append(end - start)

    #insertion
    start_insertion = timeit.default_timer()
    a = [j for j in range(1, i + 1)]
    random.shuffle(a)
    insertionsort(a)
    end_insertion = timeit.default_timer()
    times_insertion.append(end_insertion - start_insertion)


plt.plot(values, times, label="merge sort")
plt.plot(values, times_insertion, label="insertion sort")

plt.grid()
plt.legend()
plt.show()

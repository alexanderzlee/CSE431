import time
import matplotlib.pyplot as plt
import random

size = 10
sizes = [i * 1000000 for i in range(0, size)]
bstInsert = []
bstDelete = []
HashInsert = []
HashDelete = []

bstInsertTime = []
bstDeleteTime = []
hashInsertTime = []
hashDeleteTime = []
insert = random.randint(-100, 100)
delete = random.randint(-100, 100)
for i in range(size):
    # bst insert
    start = time.time()
    bstInsert.append(insert)
    end = time.time()
    bstInsertTime.append(end - start)

    # bst delete
    start = time.time()
    bstDelete.append(delete)
    end = time.time()
    bstDeleteTime.append(end - start)

    # hash insert
    start = time.time()
    HashInsert.append(insert)
    end = time.time()
    hashInsertTime.append(end - start)

    # hash delete
    start = time.time()
    HashDelete.append(delete)
    end = time.time()
    hashDeleteTime.append(end - start)

plt.title("Insertion Comparison, n = 10")
plt.xlabel("Size of data")
plt.ylabel("Time to insert")
plt.plot(sizes, bstInsertTime, label = "Binary Tree")
plt.plot(sizes, hashInsertTime, label = "Hash Table")
plt.legend()
plt.show()

plt.title("Deletion Comparison, n = 10")
plt.xlabel("Size of data")
plt.ylabel("Time to insert")
plt.plot(sizes, bstDeleteTime, label = "Binary Tree")
plt.plot(sizes, hashDeleteTime, label = "Hash Table")
plt.legend()
plt.show()

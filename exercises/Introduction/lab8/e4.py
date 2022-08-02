import random
from typing import Counter

def print_my(arr):
    for x in arr:
        print(x, end="\t")

def count_times(arr, counters):
    for x in arr:
        if(x == 0): counters[0]+=1
        elif x == 1: counters[1]+=1
        elif x == 2: counters[2]+=1
        elif x == 3: counters[3]+=1
        elif x == 4: counters[4]+=1
        elif x == 6: counters[6]+=1
        elif x == 7: counters[7]+=1
        elif x == 8: counters[8]+=1
        elif x == 9: counters[9]+=1
        elif x == 10: counters[10]+=1


n = int(input("Give the length of the array: "))

arr = []


for i in range(0, n, +1):
    arr.append(random.randint(0, 10))

counters = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print_my(arr)
print("")
count_times(arr, counters)

for i in range(0, 11, +1):
    print("%d: %d" % (i, counters[i]))

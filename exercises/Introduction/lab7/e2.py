from itertools import count
from operator import countOf
from sys import float_repr_style

def count_even(arr):
    counter = 0
    for x in arr:
        if x%2==0: counter+=1
    return counter

arr = []

print("Please enter 5 integers:  ")
for i in range(0, 5, +1):
    arr.append(int(input("[%d]: " % int(i+1))))


print("\nSUM OF EVEN INTEGERS: %d " % sum(x for x in arr if x%2 == 0))
print("NUMBER OF EVEN INTEGERS: %d " % count_even(arr))
print("AVERAGE OF EVEN INTEGERS: %.1f " % float(sum(x for x in arr if x%2 == 0) / count_even(arr)))

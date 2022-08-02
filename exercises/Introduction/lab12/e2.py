import math
import random
from re import A

def random_array(arr, n, p, q):
    for i in range(0, n, +1):
        arr.append(random.randint(p, q))


def display_array(arr):
    for i in range(0, n, +1):
        print(arr[i], end=" ")


def sum_odd(arr):
    sum = 0
    for x in arr:
        if x%2!=0:
            sum+=x
    return sum


arr = []
n = int(input("Enter length of the array: "))

print("Enter the range[p, q] ")
p = int(input("p: "))
q = int(input("q: "))

random_array(arr, n, p, q)
print("List of elements: ")
display_array(arr)
print("\nSUM OF ODDS:", sum_odd(arr))
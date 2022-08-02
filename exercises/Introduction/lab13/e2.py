from cmath import pi
import random
from reprlib import aRepr

def random_array(arr, n, p, q):
    for i in range(0, n, +1):
        arr.append(random.randint(p, q))


def display_array(arr):
    for i in range(0, n, +1):
        print(arr[i], end=" ")

def count_less(arr, x):
    counter = 0
    for i in arr:
        if i<x: 
            counter+=1
    return counter



arr = []
n = int(input("Enter length of the array: "))

print("Enter the range[p, q] ")
p = int(input("p: "))
q = int(input("q: "))

random_array(arr, n, p, q)
print("List of elements: ")
display_array(arr)
x = int(input("Enter the x:  "))
print("Number of elements less than", x, ":", count_less(arr, x))

import math
import random
from re import A

def random_array(arr, n, p, q):
    for i in range(0, n, +1):
        arr.append(random.randint(p, q))


def display_array(arr):
    for i in range(0, n, +1):
        print(arr[i], end=" ")


def avearge_odd(arr):
    counter = 0; sum = 0
    for x in arr:
        if x%2!=0:
            counter+=1
            sum+=x
    return float(sum/counter)


arr = []
n = int(input("Enter length of the array: "))

print("Enter the range[p, q] ")
p = int(input("p: "))
q = int(input("q: "))

random_array(arr, n, p, q)
display_array(arr)
print("AVERAGE OF ODDS:", avearge_odd(arr))
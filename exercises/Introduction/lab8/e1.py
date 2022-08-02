import random

def count_positive(arr):
    counter = 0
    for x in arr:
        if(x>0): counter+=1
    return counter

def print_positve(arr):
    for x in arr:
        if(x > 0):
            print(x, end="\t")


n = int(input("Give the length of the array: "))

arr = []

print("Give the range[a, b]: ")
a = int(input("a = "))
b = int(input("b = "))

for i in range(0, n, +1):
    arr.append(random.randint(a, b))

print("Numbers from the range [ %d, %d] " % (a, b))
print(arr)
print("There are %d positive numbers in the array: " % count_positive(arr))
print_positve(arr)
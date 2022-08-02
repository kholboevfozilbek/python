import random

def first_postive(arr):
    index = 0
    for i in range(0, len(arr), +1):
        if(arr[i] > 0):
            index = i
            break
    return index


def last_postive(arr):
    index = 0
    for i in range(len(arr)-1, -1, -1):
        if(arr[i] > 0):
            index = i
            break
    return index


n = int(input("Give the length of the array: "))

arr = []

print("Give the range[a, b]: ")
a = int(input("a = "))
b = int(input("b = "))

for i in range(0, n, +1):
    arr.append(random.randint(a, b))

print("Numbers from the range [ %d, %d] " % (a, b))
print(arr)
print("First positive integer is %d which is located at index %d" % (arr[first_postive(arr)], first_postive(arr)))
print("Last positive integer is %d which is located at index %d" % (arr[last_postive(arr)], last_postive(arr)))
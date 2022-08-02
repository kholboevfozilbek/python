import random

def repeating_number(arr, at=0):
    index = 0
    found = False
    for i in range(0, len(arr), +1):
        for j in range(i+1, len(arr), +1):
            if arr[i] == arr[j]:
                index = i
                at = i
                found = True
                break
        if(found == True):
            break
    return arr[index]

def print_on_repeat(arr):
    x = repeating_number(arr)
    
    for a in arr:
        if a == x:
            print("[%d]" % a, end="\t")
        else:
            print(a, end="\t")


n = int(input("Give the length of the array: "))

arr = []

print("Give the range[a, b]: ")
a = int(input("a = "))
b = int(input("b = "))

for i in range(0, n, +1):
    arr.append(random.randint(a, b))

print("Numbers from the range [ %d, %d] " % (a, b))
print(arr)

at = 0
print("Number %d recurs, first occurance is at %d " % (repeating_number(arr, at), at))
print_on_repeat(arr)
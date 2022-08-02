import random

def random_array(arr, n, p, q):
    for i in range(0, n, +1):
        arr.append(random.randint(p, q))


def display_array(arr):
    for i in range(0, n, +1):
        print(arr[i], end=" ")


arr = []
n = int(input("Enter length of the array: "))

print("Enter the range[p, q] ")
p = int(input("p: "))
q = int(input("q: "))

random_array(arr, n, p, q)
print("List of elements: ")
display_array(arr)

x = int(input("\n\nEnter x to search from the list: "))
print(x, " occurs %d times in the list: \n" % arr.count(x))
print(x, "first ocurance is at index", arr.index(x))
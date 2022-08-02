
def input_array(arr, n):
    print("Please enter %d elements" % n)
    for i in range(0, n, +1):
        arr.append(int(input(": ")))


def average(arr, n):
    return float(sum(arr)/n)


def count_odd(arr):
    counter = 0
    for i in arr:
        if i%2 != 0: 
            counter+=1
    return counter

arr = []
n = int(input("Enter the length of the array:  "))

input_array(arr, n)
print("Average: ", average(arr, n))
print("Number of odds: ", count_odd(arr))
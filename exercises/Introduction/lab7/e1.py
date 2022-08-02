
arr = []

print("Please enter 5 integers:  ")
for i in range(0, 5, +1):
    arr.append(int(input("[%d]: " % int(i+1))))


print("\nSum: %d " % int(sum(arr)))
average = float(sum(arr)/len(arr))
print("Average: %.1f " % average)
print("Number of integers greater than %.1f = %d " % (average, sum(i>average for i in arr)))
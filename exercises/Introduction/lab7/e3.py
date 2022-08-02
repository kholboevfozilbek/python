arr = []

print("Please enter 5 integers:  ")
for i in range(0, 5, +1):
    arr.append(int(input("[%d]: " % int(i+1))))

print("LARGEST INTEGER: %d" % int(max(arr)))
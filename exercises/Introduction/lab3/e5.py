
n = int(input("Enter n: "))
start = 1; sum = 0
for i in range(0, n, +1):
    sum += start
    print(start, end=" ")
    start += 2

print("\nSum: ", sum)
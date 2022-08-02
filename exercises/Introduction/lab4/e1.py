import sys
m = int(input("Enter a positive integer: "))

if m < 1:
    sys.exit("Enter POSITIVE integer!!!")

sum = 0; counter = 0; i = 1
while sum <= m:
    sum += i
    print(i, end=" ")
    counter += 1
    i += 1
print("\nSUM: ", sum)
import sys
x = int(input("Enter a positive integer: "))

if x < 1:
    sys.exit("Enter POSITIVE integer!!!")

str_val = str(x)
sum = 0
for i in range(0, len(str_val), +1):
    sum += int(str_val[i])
    print(str_val[i], end="+")
print("\nSUM: ", sum)
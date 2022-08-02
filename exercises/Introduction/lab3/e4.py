n = int(input("Enter the number:  "))
m = int(input("Up to:  "))
for i in range(1, m+1, +1):
    print("%d * %d = %d" % (n,i,n*i))
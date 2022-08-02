import math

x = int(input("Enter 1st int:  "))
y = int(input("Enter 2nd int:  "))

print("GCD[%d, %d] = %d" % (x, y, math.gcd(x, y)))
print("LCM[%d, %d] = %d" % (x, y, math.lcm(x, y)))
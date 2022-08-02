import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("GCD[%d, %d] = %d" % (a, b, math.gcd(a, b)))
print("LCM[%d, %d] = %d" % (a, b, math.lcm(a, b)))
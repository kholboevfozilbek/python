
import math
print("We solve quadratic equation in form ax^2 + bx + c = 0")
print("Please provide the coefficients-> a  b  c")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: ")) 

square_positive = math.sqrt(abs(pow(b, 2) - 4*a*c))

x_1 = (-b + square_positive) / 2*a
x_2 = (-b - square_positive) / 2*a

print("x_1 =", x_1)
print("x_2 =", x_2)
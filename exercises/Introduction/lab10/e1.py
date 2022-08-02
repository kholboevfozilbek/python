import math

def hypotenuse(a, b):
    return math.sqrt(math.pow(a, 2) + math.pow(b, 2))

a = float(input("Enter a leg: "))
b = float(input("Enter b leg: "))

print("\nhypotenuse: %.2f " % hypotenuse(a, b))
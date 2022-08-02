import math

def valid_sides(a, b, c):
    if(a+b <= c or a+c <= b or b+c <= a): 
        return False
    return True


def perimeter(a, b, c):
    return a+b+c

def area(a, b, c):
    s = a+b+c/2.0
    return math.sqrt(s*(s-a)*(s-b)*(s-c)) 


print("Enter 3 sides of triangle")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if valid_sides(a,b,c):
    print("Circumference: %.1f" % perimeter(a, b, c))
    print("Area: %.2f" % area(a, b, c))
else:
    print("Sides %.1f %.1f %.1f can NOT make triangle" % (a, b, c))
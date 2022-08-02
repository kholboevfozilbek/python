a,b,c = map(int, input("Enter 3 integers seperated by whitespace:  ").split())

print("Sum: %d" % int(a+b+c))
print("Average: %.1f" % float((a+b+c)/3.0))
print("Product: %d" % int(a*b*c))
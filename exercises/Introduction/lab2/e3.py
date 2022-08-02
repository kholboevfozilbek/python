x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))

print(x, "is larger") if x>y else print(y, "is larger") if y>x else print("Numbers are equal")
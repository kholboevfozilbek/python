"""
num = float(input("Enter an value: "))
print("Value ", num)
print("Type",type(num))

# multiple input of the same type
a, b = map(int, input("Enter 2 ints: ").split())
print("Values", a, b) 

q, r, s = input("Enter 3 values: ").split()
print("Values ", q, r, s)
print("Type q: ", type(q))
print("Type r: ", type(r))
print("Type s: ", type(s)) 

# giving sperator and maxsplit
a,b,c = input("Enter 3 values: ").split(";", 3)
print("Values: ", a,b,c)
print("Type a: ", type(a))
print("Type b: ", type(b))
print("Type c: ", type(c)) 

# USING List 

# with map and where all of them becomes ints
x = list(map(int, input("Enter ints: ").split()))
print("List: ", x)
print("Type: ", type(x)) """

# without map where you can take any datatype but all are treated as string
x = list(input("Enter values: ").split())
print("List: ", x)
print("Type: ", type(x[3]))
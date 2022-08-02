print("GFG")  # \n newline added by default
print('G','F','G') # , sperates contents with softspaces by default

# we can change those default features

print("GFG", end = "@")  # ends with @ 
print('G', 'F', "G", sep='#')  # seperates the contents with #

# FORMATTING THE OUTPUT

# using f
name = "Fozil"
age = 18
print(f"Hello {name}! You are {age}?")

a = 20
b = 10

# using format()
print("a={} and b={}".format(a, b))

# using % operator

char = 'A'
print("sum = %i" % 5)
print("letter is %c" % char)

word = "Subhana Robbial Azim"
marta = 3
print("%s %d times" % (word, marta))
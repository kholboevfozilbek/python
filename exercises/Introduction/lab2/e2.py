x = int(input("Enter some integer value: "))

if(x > 9 and x < 100):
    print(x, "is a two-digit number")
elif(x < -9 and x > -100):
    print(x, "is a two-digit number")
else:
    print(x, "is not a two-digit number")
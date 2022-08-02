
x = int(input("Enter number: "))

s = str(x)
carry = 0
for i in range(len(s)-1, -1, -1):
    x = int(s[i])
    if x == 9:
        x = 0
        s[i] = str(x)
        carry = 1
    else:
        x+=1
        x+=carry
        carry = 0
    
print(s) 

from statistics import quantiles


x = int(input("Enter an integer [6-digis at max]: "))

str_val = str(x)
equal = True
for i in range(0, len(str_val), +1):
    if i != len(str_val)-1:
        if str_val[i] != str_val[i+1]:
            equal = False
            break
if equal == True:
    print("\nALL digits are SAME")
else:
    print("\nNOT SAME")
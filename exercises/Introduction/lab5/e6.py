import math
from pickletools import read_decimalnl_long
from sys import float_repr_style
ch = 'y'
i = 1
sum_pos = 0; count_pos = 0; sum_neg = 0; count_neg = 0
while ch == 'Y' or ch == 'y':
    print("Enter real numbers")
    real = float(input("%d. Give a number: " % i))
    if real > 0:
        print("Square root: %f " % float(math.sqrt(real)))
        sum_pos += real
        count_pos+=1
    else:
        print("Square: %f " % float(math.pow(real, 2)))
        sum_neg += real
        count_neg+=1
    ch = input("Continue [y/n]: ")
    i+=1

print("\nSum of positives:", sum_pos)
print("Average of positives:", float(sum_pos/count_pos))
print("Sum of negatives:", sum_neg)
print("Average of negatives:", float(sum_neg/count_neg))
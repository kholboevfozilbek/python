from cmath import cos
from traceback import print_tb


cost = float(input("Enter cost price of  the item:  "))
sell = float(input("Enter selling price of  the item:  "))

if sell>cost:
    print("%.1f profit" % float(sell-cost))
elif cost>sell:
    print("%.1f loss" % float(cost-sell))
else:
    print("No profit No loss")
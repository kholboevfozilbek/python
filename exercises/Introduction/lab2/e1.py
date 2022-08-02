q = int(input("Enter quantity: "))
p = float(input("Enter price per item:  "))

if(q*p > 5000):
    print("Total expense with discout:  %.1f" % float(q*p))
else:
    print("Total expense: %.1f " % float(q*p))
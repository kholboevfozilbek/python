import sys
fee = 2500
increase = float(input("Enter % increase [0-10]: "))

if increase<0 or increase>10:
    sys.exit("Increase % is in between 0-10")

for i in range(0, 6, +1):
    fee += fee*(increase/100)
    print("Next %d year: %.1f" % (i+1, fee))
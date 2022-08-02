import sys
cal = float(input("Enter number of calorise burned per minute: "))

if cal<1:
    sys.exit("please enter valid number of calories burned per minute")
for i in range(5, 31, +5):
    print("After %d minutes: %.1f" % (i, cal*i))
    cal*i
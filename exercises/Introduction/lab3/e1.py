import sys
rise = 1.5
year = int(input("Enter number of years: "))

if year < 1:
    sys.exit("Enter valid year!")
for i in range(0, 25, +1):
    print("year %i: %.1f" % (i+1, rise))
    rise += 1.5
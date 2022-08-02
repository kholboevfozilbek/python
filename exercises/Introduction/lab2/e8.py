
import datetime

print("Enter dates in format dd:mm::yyyy in correct number format")

day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year  = int(input("Enter the year: "))

d = int(input("Enter the day: "))
m = int(input("Enter the month: "))
y  = int(input("Enter the year: "))


y1 = datetime.datetime(year,month, day)
y2 = datetime.datetime(y,m, d)

if y1 < y2:
    print(y1, "is earlier")
elif y2 < y1:
    print(y2, "is earlier")
else:
    print("The dates are the same")
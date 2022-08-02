
temp = float(input("Enter number of hours worked (-1 to end): "))

while temp != -1:
    print("Accrued leave: %d " % round(float(2+(temp*0.1))))
    temp = float(input("Enter number of hours worked (-1 to end): "))

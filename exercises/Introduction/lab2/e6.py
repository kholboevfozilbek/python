year = int(input("Enter the year: "))

if (year%4 == 0):
    if(year%100 != 0):
        if(year%400 == 0):
            print(year, "IS LEAP year")
        else:
            print(year, "is NOT leap year")
    else:
        print(year, "is NOT leap year")
else: 
    print(year, "is NOT leap year")
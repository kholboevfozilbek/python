from math import factorial


print("Temprature converter from celsius to kelvin and fahrenheit")

temp = input("Enter temprature: ")
print("----------------------------------") 
print(temp, "celsius = %.1f kelvin" % float(float(temp) + float(273.15)))
print(temp, "celsius = %.1f fahrenheit" % float(float(32) + float(9/5) * float(temp)))

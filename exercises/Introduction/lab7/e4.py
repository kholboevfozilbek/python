from sys import float_repr_style


print("Please enter 10 persons salaries: ")


arr = []


for i in range(0, 10, +1):
    arr.append(float(input("[%d]: " % int(i+1))))

min = float(min(arr))
max = float(max(arr))
average = float(sum(arr)/len(arr))
count_min = 0; count_max = 0
min_persons = []
max_persons = []
print("LOWEST SALARY: %.2f " % min)
print("HIGHEST SALARY: %.2f " % max)
print("AVERAGE OF SALARIES: %.2f " % average)

print("LIST OF PERSONS SALARIES GREATER THAN %.2f :" % average)


for i in range(0, len(arr), +1):
    if(arr[i]>average):
        print("Person %d: %.2f " % (int(i+1), arr[i]))
    elif (arr[i] == min): 
        count_min+=1
        min_persons.append("Person %d" % int(i+1))
    elif (arr[i] == max): 
        count_max+=1
        max_persons.append("Person %d" % int(i+1))


print("LOWEST SALARY: %.2f - " % min, end="")
for p in min_persons:
    print(p, end="; ")

print(" [ %d persons ]" % count_min)

print("HIGHEST SALARY: %.2f - " % max, end="")
for p in max_persons:
    print(p, end="; ")

print(" [ %d persons ]" % count_max)
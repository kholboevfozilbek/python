budget = float(input("Enter amount budgeted for month:  "))
x = float(input("Enter an amount spent (non-positive value to end): "))
total = 0
while x > 0:
    total += x
    x = float(input("Enter an amount spent (non-positive value to end): "))

print("Budget: ", budget)
print("Spent: ", total)

if total < budget:
    print("You are %.1f under budget. WELL DONE!" % float(budget-total))
else:
    print("You are %.1f over budget. PLAN BETTER NEXT TIME!" % float(total-budget))
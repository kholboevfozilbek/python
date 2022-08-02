for i in range(0, 6, +1):
    print(i)
    break
else:
    print("else block  is executed when loop finishes itself")
print("is not executed when loop is stopped by break statement")
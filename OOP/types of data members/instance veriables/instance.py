

class Employee:

    def __init__(self, n, s, e):
        self.name = n
        self.salary = s
        self.email = e
    
    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Email:", self.email)

e = Employee("Adil Noor Khan", 4500, "Adil.Khan@harman.com")

e.display()
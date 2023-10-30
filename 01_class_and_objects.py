# Representation of class and its objects

# Creating a class
class Employee():
    def __init__(self, fname, lname, salary):   # Creating a constructor
        self.fname = fname
        self.lname = lname
        self.salary = salary

# Creating the objects of the class
erl = Employee("Erling", "Haaland", 2000)
jck = Employee("Jack", "Grealish", 1900)

print(erl.fname)
print(jck.salary)
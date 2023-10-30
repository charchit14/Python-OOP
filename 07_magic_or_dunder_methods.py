class Employee():
    
    increment = 2
    
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increase(self):
        self.salary = self.salary * self.increment

    # Defining a dunder/magic method
    def __add__(self, other):
        return self.salary + other.salary
    
    # When we print an object then it will show the string representation of that object
    def __repr__(self):
        return 'Employee({}, {}, {})'.format(self.fname, self.lname, self.salary)

    # Creating anothe dunder method with the name '__str__'
    def __str__(self):
        return f"The first name of the Employee is: {self.fname}"


erl = Employee("Erling", "Haaland", 2000)
jck = Employee("Jack", "Grealish", 900)

# Use of dunder method (add)
print(erl+jck)

# Use of '__repr__' method
print(repr(jck))

# Use of '__str__'
print(str(erl))
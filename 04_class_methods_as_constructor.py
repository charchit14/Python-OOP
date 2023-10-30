class Employee():
    
    increment = 2
    
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increase(self):
        self.salary = self.salary * self.increment

    # Alternative method
    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary)


erl = Employee("Erling", "Haaland", 2000)

# Object of the class
jck = Employee.from_str("Jack-Grealish-900")

print(jck.fname, jck.lname, jck.salary)
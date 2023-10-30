class Employee():
    
    increment = 2
    
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increase(self):
        self.salary = self.salary * self.increment

    # Creating a class method, this takes class as an argument
    @classmethod
    def change_increment(cls, amount):
        cls.increment = amount


erl = Employee("Erling", "Haaland", 2000)
jck = Employee("Jack", "Grealish", 900)

print(f"Before increment: {jck.salary}")

# Calling the class method using 'Employee' class so, it sets the variable 'increment' to whatever the value is passed (9 in this case)
Employee.change_increment(9)    
jck.increase()
print(f"After increment: {jck.salary}")
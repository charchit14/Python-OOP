class Employee():
    
    increment = 2
    
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increase(self):
        self.salary = self.salary * self.increment
    

# The class 'Players' inherits all the methods and attributes of class 'Employee' (with additional parameters) 
class Players(Employee):
    def __init__(self, fname, lname, salary, position, goals):
        super().__init__(fname, lname, salary)  # This 'super()' will inherit all the attributes of parent class's constructor
        self.position = position
        self.goals = goals

    def increase(self):
        self.salary = self.salary * (self.increment + 9.11)
        return self.salary


erl = Players("Erling", "Haaland", 2000, "ST", 36)

print(erl.goals)
print(erl.increase())
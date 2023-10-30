# We use 'static method' to make independent function and when we want to pass only those arguments that we desire in that function

class Employee():
    
    increment = 2
    
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increase(self):
        self.salary = self.salary * self.increment
    
    @classmethod
    def change_increment(cls, amount):
        cls.increment = amount
    
    # Creating a static method that checks whether the office will be open or not depending upon day
    @staticmethod
    def isopen(day):
        if day == 'Saturday':
            return False
        else:
            return True


erl = Employee("Erling", "Haaland", 2000)
jck = Employee("Jack", "Grealish", 900)

print(Employee.isopen("Tuesday"))
print(erl.isopen("Saturday"))
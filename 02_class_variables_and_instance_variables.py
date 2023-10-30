# # Demonstration 1

# # Creating a class
# class Employee():

#     increment = 2

#     def __init__(self, fname, lname, salary):
#         self.fname = fname
#         self.lname = lname
#         self.salary = salary

#     def increase(self):
#         self.salary = self.salary * Employee.increment
    
#     '''
#     'Employee.increment' this makes sure that the increment variable is choosen directly from the Employee class (i.e. in this case 'increment' is a class variable).
#     If we write 'self.increment' then it will be an instance variable not a class variable
#     so, it first will search the 'increment' variable in the instacnes of the class and if not found then only it will come back to class varibale.
#     '''

# # Creating the objects of the class
# erl = Employee("Erling", "Haaland", 2000)
# jck = Employee("Jack", "Grealish", 1900)

# print(jck.salary)
# jck.increase()
# print(jck.salary)


# Demonstration 2 (showing how the behaviour changes when instance variable is used)

class Employee():
    increment = 2
    number_of_employee = 0

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.increment = 3  # Creating an instance variable
        Employee.number_of_employee += 1

    def increase(self):
        self.salary = self.salary * self.increment  # Here is the change
        

print(Employee.number_of_employee)

erl = Employee("Erling", "Haaland", 2000)
jck = Employee("Jack", "Grealish", 1900)

print(Employee.number_of_employee)

print(jck.salary)
jck.increase()
print(jck.salary)

# # This will show all the instance variables of jck
# print(jck.__dict__)

# # This will show all the instance variables of the Employee class
# print(Employee.__dict__)
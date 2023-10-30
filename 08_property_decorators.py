class Employee():
    
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    # Function to adjust the email if there is change in the 'fname' or 'lname'
    # '@property' ensures that this function now acts as an attribute and we can call it by using it as an attribute 
    @property
    def mail(self):
        if self.fname == None:
            return 'Email not found'
        else:
            return self.fname + '.' + self.lname + '@pmail.com'
    
    # Setter method to set the email accordingly i.e. in whichever format is asked by user ('lname.fname@pmail.com' in this case)
    @mail.setter
    def mail(self, new_mail):
        first_cut = new_mail.split('@')[0]
        second_cut = first_cut.split('.')
        self.fname = second_cut[0]
        self.lname = second_cut[1]

    # To delete an email
    @mail.deleter
    def mail(self):
        self.fname = None
        self.lname = None

erl = Employee("Erling", "Haaland", 2000)
jck = Employee("Jack", "Grealish", 900)

print(erl.mail)
print(jck.mail)
print()

# Considering there is change in 'lname'
jck.lname = "JG"
print(jck.mail)

# Now if someone wants their email to be 'lname.fname@pmail.com'
jck.mail = 'JG.Jack@pmail.com'
print(jck.mail)

# Deleting an email (calls 'deleter')
del jck.mail
print(jck.mail)
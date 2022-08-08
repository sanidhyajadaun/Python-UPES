print('---------------------------------------------------------------------------------------')
class Employee:      #class definition
    def __init__(self,first,last,pay):         #class constructor
        #assigning the passed values 
        self.first_name=first
        self.last_name=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'    #generating the email
    def display(self):   #displaying the details through the method display()
        print("First name : ",self.first_name)
        print("Last Name  : ",self.last_name)
        print("Pay        : ",self.pay)
        print("Email      : ",self.email)

emp1=Employee("Mohandas","Gandhi",50000)   #object created
emp1.display()       #method display called
print('---------------------------------------------------------------------------------------')


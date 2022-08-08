print('---------------------------------------------------------------------------------------')
class Vehicle:    #class definition
    def __init__(self,name,max_speed,mileage,color="white"):  #class constructor
        #assigning the instance attributes
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
        self.color=color
    def seating_capacity(self,capacity):    #method seating_capacity 
        self.capacity=capacity
        return f'The seating capacity of a {self.name} is {self.capacity} passengers'

class Bus(Vehicle):   #definition of inherited class of Vehicle
    def __init__(self,name,max_speed,mileage,color="white"):
        super().__init__(name,max_speed,mileage,color="white")
        self.capacity=50     #setting the default capacity as 50
    def display(self):       #displaing the details
        print("Name      : "+self.name)
        print("Max Speed : ",self.max_speed)
        print("Mileage   : ",self.mileage)
        print("Color     : "+self.color)
        print("Capacity  : ",self.capacity)

obj=Bus("Volvo",60,20)    #object created
obj.display()             #displaying the details
print("\nUpdating the seating capacity...!")
print(obj.seating_capacity(90))
print("\nDisplaying the modified details....!")
obj.display()
print('---------------------------------------------------------------------------------------')

# in aggregation we build a relationship between two or more classes to represent a whole-part relationship
# in aggregation, the part class is independent of the whole class
# aggregation is a weak relationship

# here we are going to create a class called vehicle and a class called Employee
# Employee "has a " vehicle
# Employee class is the whole class and vehicle class is the part class
class vehicle:
    def __init__(self, name, color, liscence_plate , is_electric):
        self.name = name
        self.color = color
        self.liscence_plate = liscence_plate
        self.is_electric = is_electric

    def show_liscece_plate(self):
        print(f"Liscence Plate: {self.liscence_plate}")

    
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Color: {self.color}")
        print(f"Liscence Plate: {self.liscence_plate}")
        print(f"Is Electric: {self.is_electric}")

    
class Employee:
    def __init__(self, name, age, vehicle):
        self.name = name
        self.age = age
        self.vehicle = vehicle

    # employee will have a vehicle attribute which will be an object of the vehicle class
    # this is how we create an aggregation relationship between the two classes

    def show_vehicle_info(self):
        print("Vehicle Information")
        self.vehicle.show_info()
    

vehicle1 = vehicle("Toyota", "Red", "ABC123", is_electric = False) # we can also pass the name of a boolean variable in the argument
# we could have wrote just false instead of is_electric = False
employee1 = Employee("John", 30, vehicle1)
# here we are passing the object of vehicle class as the argument to the employee class
employee1.show_vehicle_info()
print(employee1.vehicle.color)
print(employee1.vehicle.show_liscece_plate())
# we can access the attributes of the vehicle class using the object of the employee class
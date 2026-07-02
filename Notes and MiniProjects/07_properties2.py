class Backpack:
    def __init__(self):
        self._items = []

    def get_items(self):
        return self._items
    
    def set_items(self , newItems):
        if isinstance(newItems, list): # check if newItems is a list or not
            self._items = newItems
        else:
            raise TypeError("please enter a valid list of items")
# it won't set the items list if the given arguments is a string or not a valid list        

my_backpack = Backpack()
print(my_backpack.get_items())
my_backpack.set_items(["book", "pen", "laptop"])
print(my_backpack.get_items())

class Circle:
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, float) and new_radius > 0:
            self._radius = new_radius
        else:
            raise ValueError("please enter a valid radius(float) greater than 0")
        

my_circle = Circle(5) # 5is a valid value
print(my_circle.get_radius())
my_circle.set_radius(6.5) # 6.5 is a valid value
print(my_circle.get_radius())

class Dog:
    def __init__(self, age):
        self._age = age


    def get_age(self):
        print("callling the getter") # we are using this statement to make sure when the getter is called it is printed
        return self._age

    def set_age(self, new_age):
        print("calling the setter") # we are using this statement to make sure when the setter is called it is printed
        if isinstance(new_age, int) and 0 < new_age < 30:
            self._age = new_age
        else:
            raise ValueError("please enter a valid age(integer) between 0 and 30")

    # to make the ussage of the class more readable we can use property 
    age = property(get_age, set_age)

my_dog = Dog(5) # 5 is a valid value
print(f"my dog is now {my_dog.age} years old")
print("one year later")
my_dog.age += 1
print(f"my dog will be {my_dog.age} years old")

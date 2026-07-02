import math
# we can also use the from keyword to import the specific object from a module like this 
# from math import pi
from random import randint
# this statement imports the math module, which contains the pi object

# this statement imports the random module, which contains the randint function
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius
    

# a = random.randint(1, 10) (we will write this when we import the whole module )
a = randint(1, 10) # we write this when we only import the specific object from the module
my_circle = Circle(a)
print(f"Circle with radius {my_circle.radius} has area {my_circle.area()} and circumference {my_circle.circumference()}")
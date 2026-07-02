# aliases are two objects which point to the same memory location in a python program
# Aliasing is a very useful feature in python, but it can also be very dangerous.
# When you make a change to an object using one alias, the change is reflected in the other alias as well.
# If you want to modify an object and keep a copy of the original, you need to make a copy of the object.
a = [1, 2, 3]
b = a
# now both of these objects are aliases of each other
# we can also have more than one aliases of the same object in the same program

class Circle:
    def __init__(self, radius):
        self.radius = radius


my_circle = Circle(5)
another_circle = my_circle # (the object another_circle is not the copy of my circle . it is pointing to the same memory location as my_circle)
# so its like the 2nd name of my_circle object 
# now both of these objects are aliases of each other
# but if we make a change in another_circle, it will also be reflected in my_circle, this can be a potential source of bugs in our program


class Circle:

    VALID_COLORS = ["red", "green", "blue", "yellow", "black", "white", "purple", "pink", "orange"]
# defining class constants* (class variables) that are shared by all instances of the class
# *class constants are variables that are defined in a class but are not intended to be changed
    def __init__(self, radius, color):
        self._radius = radius
        self._color = color

    def get_radius(self):
        return self._radius
    
    def set_radius(self, new_radius):
        if isinstance(new_radius, float) and new_radius > 0:
            self._radius = new_radius
        else:
            raise ValueError("please enter a valid radius(float) greater than 0")
        
    def get_color(self):
        return self._color
    
    def set_color(self, new_color):
        if new_color in Circle.VALID_COLORS:
            self._color = new_color
        else:
            raise ValueError("please enter a valid color")
        
    radius = property(get_radius, set_radius)
    color = property(get_color, set_color)

my_circle = Circle(5, "red") # 5 is a valid value and red is a valid color
print(my_circle.get_radius())
print(my_circle.get_color())
my_circle.set_radius(6.5) # 6.5 is a valid value
my_circle.set_color("blue") # blue is a valid color
print(my_circle.get_radius())
print(my_circle.get_color())

#  the @property decorator can be used to define a getter method for a property
# it is basically a functyion that takes a function as an argument and returns a new function that behaves like a property
# it cannot be used to define a setter method
# it extensds the behavious of the function without explicitly modifying the function

class Movie:
    def __init__(self, title, rating):
        self.title = title # the title is a public attribute
        self._rating = rating # the rating is a non public attribute

    @property
    def rating(self):
        print("calling the getter")
        return self._rating
    # here we use the same syntax we use in a getter , but with the @property decorato

    @rating.setter
    def rating(self, new_rating):
        print("calling the setter")
        if isinstance(new_rating, float) and 0 < new_rating < 10:
            self._rating = new_rating
        else:
            raise ValueError("please provide a valid rating(float) between 0 and 10")


Favourite_Movie = Movie("The Godfather", 9.2)
print(Favourite_Movie.title)
print(Favourite_Movie.rating)
# the rating attribute is now a property and can be accessed like an attribute even though it is a non public attribute
Favourite_Movie.rating = 9.5
print(Favourite_Movie.rating)
# the rating attribute can be set like an attribute even though it is a non public attribute just like a setter method

class Backpack:
    def __init__(self,):
        self._items = []

    
    @property
    def items(self): #this is getter
        print("calling the getter.....")
        return (self._items)
    
    @items.setter
    def items(self, new_items): #this is setter
        print("calling the setter.....")
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print("Please provide a valid list of items")


my_backpack = Backpack()
my_backpack.items= ["laptop", "phone", "charger", "Water bottle"]
print(my_backpack.items)
my_backpack.items = ["Sleeping Bag", "Coffee", "Milk", "Bread"]
print(my_backpack.items)
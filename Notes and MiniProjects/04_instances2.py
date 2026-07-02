class Circle :
    def __init__(self, radius) :
        self.radius = radius
        self.color = "Blue"

class Rectangle :
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Movie :
    def __init__(self, title, year, language, rating):
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating

# creating instances / objects on the bases of a class
# self parameter is automatically skipped while giving arguments

class Backpack : 
    def __init__(self ):
        self.items = [] 
        # self.brand = brand
        # self.color = color
        # self.size = size
   

# example of instance with no argument
my_backpack = Backpack()
# print(my_backpack) it will return that the backpack is an object in 000xxxx  location in the memory
print(my_backpack.__dict__) # it will return the dictionary of the object with all the attributes

my_circle = Circle(4)
# print(my_circle) this will return the location of circle object in memory

my_rectangle = Rectangle(23, 43)
print(my_rectangle) # this will return the location of rectangle object in memory

# none keyword in python 
#  None is a keyword in python which is used to represent the absence of a value
#  None is an object in python and it is a singleton object which means there is only one
#  None object in python
#  None is a subclass of all classes in python
#  None is a singleton object which means there is only one None object in python

# if there is no return statement in the function or class it will return none value

# accessing instances attributes in python
# we can access the attributes of an instance using the dot operator in python aka dot notation
# we can also use the getattr() function to access the attributes of an instance in python

class Backpack1 :
    def __init__(self):
        self.items = ["Water bottle","Pencils"]
        # print(self.items)

bc2 = Backpack1()
print(bc2.items)

favorite_movie = Movie("Pursuit of Happyness", 2010, "English", 4.7 )
print("My favorite movie")
print(favorite_movie.title) # it will return the title of the movie
print(favorite_movie.year) # it will return the year of the movie
print(favorite_movie.language) # it will return the language of the movie
# an instance is an object created from the class
# an instance has its own set of attributes and methods    ( variables)
# for example a backpack class may have a zipper count , material , no of pockets and other attributes as well 
class House :
    # the init method is used to define the initial state of an object 
    # it is called automatically when the object is called
    # def keyword is used to indicate that this will be a method in this class 
    # the methods in class should be indented (meaning that they should be given 4 spaces before the line or one tab space)   
    def __init__(self, address, price): # space after comma is necessary here
        self.address = address
        self.price = price # writing self is necessary here
        #  this means to take the price as an argument and assign that price value to the price attribute of this element / instance / object
#  self should always be the first parameter of the init methods
# we can just write self in the init attribute
        self.items = [] #type is a keyword
        # this means that the items of this class contains an empty list  
# self is used to refer to the current instance / object of a class


class Backpack : 
    def __init__(self, brand, color, size):
        self.brand = brand
        self.color = color
        self.size = size
        self.items = [] 
        # in the first line brand on RHS is the parameter defined above while self.brand refers it to the object
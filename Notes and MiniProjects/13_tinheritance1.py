class Polygon :
    def __init__(self, sides, color):
        self.sides = sides
        self.color = color

    def get_sides(self):
        return self.sides
    
# inheritance if the subclass does not have an init method

class Square(Polygon) :
    pass #we used pass statement to avoid an empty invalid class 
    # def __init__(self, sides, base, height):
    #     super().__init__(sides)
    #     self.base = base
    #     self.height = height

    # def get_area(self):
    #     return 0.5 * self.base * self.height

my_square =  Square(5 , "black")
# now this object will have thos eattribues of polyfgon class due to inheritance
print(my_square.sides)
print(my_square.color)


# Inheritance if the subclass has an init method

class Triangle(Polygon):
# lets create a class constant
    NUM_SIDES = 3

    def __init__(self, base, height , color):
        super().__init__(Triangle.NUM_SIDES , color)
        # or we can also write Polygon.__init__
        # while using the super keyword we dont need to pass the self keyword in argument
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

my_triangle = Triangle(4 , 5 ,"Blue")
print(my_triangle.color)
print(my_triangle.base)
print(my_triangle.height)
print(my_triangle.sides)
print(my_triangle.get_area())
print(my_triangle.NUM_SIDES)
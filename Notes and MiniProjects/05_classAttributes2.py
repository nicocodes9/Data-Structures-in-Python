class Circle:

    radius= 4 # here the radius is the class attribute 
    
    def __init__(self, color):
        self.color = color 
        # while attributes in the init method belongs to the instances

Circle.radius= 6
print(Circle.radius)  # Output: 6 
# its because we can manipulate the values os class attributes but it will  affect all the instances
# if we want to change the radius of a specific circle we should use instance attributes

my_circle = Circle("blue")
print(my_circle.radius)  # Output: 6
# now similarly the class arrtibutes can be changed and accessed outside of the class

class Movie:

    idcount = 1

    def __init__(self, title, director):
        self.title = title
        self.director = director
        self.id = Movie.idcount #we can also access the class attributes inside of the class
        Movie.idcount += 1
# firstly the mmethod is searched in the class itself
# if not found then it is searched in the parent class
# if not found then it is searched in the parent class of the parent class
class Polygon:

    def  __init__(self , sides , color):
        self.sides= sides
        self.color = color


    def get_sides(self):
        return self.sides
    
    
class Triangle (Polygon):

    number_of_sides = 3

    def __init__(self , color , height , base):
        super().__init__( Triangle.number_of_sides , color)
        self.height = height
        self.base = base


    def get_height(self):
        return self.height
    

# now lets create an instance of the triangle class and call the methods
my_triangle = Triangle("blue" , 5 , 4)
print(my_triangle.color)
print(my_triangle.get_sides())

# method overriding happens when the function with the same name exists in both subclass and the superclass ,
# when we call that method the subclass method will be callled and preffered over the superclass method
class Teacher:

    def __init__(self , name , subject):
        self.name = name
        self.subject = subject
    
    def welcome_students(self):
        print(f"Welcome to the {self.subject} class. My name is {self.name}.")

class Science_teacher(Teacher):
        
    def welcome_students(self):
        super().welcome_students() # this will call the welcome_students method of the parent class
        # Teacher.welcome_students(self) this will aslo do the same
        # calling the parent class method
        # now the below written code will extend te functionality of tis method
        print(f"Please make sure to wear your lab coats and goggles before entering the {self.subject} lab.")
    

# now lets create an instance of the Science_teacher class and call the method
science_teacher = Science_teacher("Emily" , "Chemistry")
science_teacher.welcome_students()
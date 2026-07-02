class Student:
    def __init__(self, name, ID, age, CGPA):
        self.name = name
        self._ID = ID  #now i have made this variable protected to tell the other devs not to change it
        self._age = age
        self.CGPA = CGPA


Student_Nora = Student("Nora", 123, 20, 3.5)
print(Student_Nora._ID)  # 123 we can accessthe protected ID attribute but we can't change it
Student_Nora._ID = 456 # we can change it but it is not recommended
print(Student_Nora._ID)  # 456
# print(Student_Nora.age) # AttributeError: 'Student' object has no attribute 'age' because _ is a protected attribute and can be accessed but not changed 


#   **** NAme Mangling in Python ****
# Python name mangling is a way to make attributes of a class hidden from other classes. It is used to prevent the accidental modification of the names of the variables. This method makes a local variable of the class hidden from the other classes, and the class can be accessed only with the help of the object of the class.
#   **** Example ****
class Employee:
    def __init__(self, name, ID, age, Salary):
        self.name = name
        self.__ID = ID  #now i have made this variable private to tell the other devs not to change it
        self.__age = age
        self.Salary = Salary


Employee_Nora = Employee("Nora", 123, 20, 5000)
# print(Employee_Nora.__ID)  # AttributeError: 'Employee' object has no attribute '__ID' because it is a private attribute
print(Employee_Nora._Employee__ID)  # 123 we can access the private ID attribute by using the name mangling method
# its technically possible to access it also but we should not do it
# name manglisg should only be used for special use cases

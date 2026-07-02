# in python every thing is an object
# even without creating a class, we can create an object
# object is also an instance of a class

# each object has an id which is its memory address
print(id(10))
# now this will print the memory address of the object 10
# we havent created any object here, but 10 is an object and it will have a uniue memory addressthroughout the lifetime of the program

# is operator is the identity comparison operator, it returns true if the memory address of the two objects are same
# print(10 is 10)
# this will
# 1. create an object 10
# 2. create another object 10 and compare both the memory addresses

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b) #this will print false
print (a == b) # this will print true
# a and b are two different objects, so a is b is false
# but the values of a and b are same, so a == b is true

# python optimizes memory usage by storing two sepeprate string variables which contain the same string value at the same memory location
# this is called string interning
c = "hello"
d = "hello"
print(c is d) # this will print true

# here a and b are two different objects, but they have the same memory address
# this is because python has stored the string "hello" in a single memory location and both a and b are pointing to the same
# memory location
print(id(c))
print(id(d))
# even their ids will point at the same memory location
# small integers (range -5 to 256) variables with the same value will be the same object in memory
e = 10
f = 10
print(e is f) # this will print true
# here a and b are two different objects, but they have the same memory address

# strings are immutable and they cannot be changed once they are created
# string interning and memory optimization can vary depending on the environment which we are using to run he python code

# in python objects are passed as referneces to functions
# so tyhat if any modificationsa re mad eto the object in the function, it will be reflected in the original object stored in the menory

my_list = [1, 2, 3]
def print_data(data):
    print("inside the function" , id(data))
    for i in data:
        print(i)
    

print_data(my_list)
print("outside the function", id(my_list))
    
# this will print the memory address of the object my_list
# here the object my_list is passed as a reference to the function print_data
# so any changes made to the object in the function will be reflected in the original object stored in the

def multiply_by_two(data):
    for i in range(len(data)):
        data[i] = data[i] * 2

multiply_by_two(my_list)
print(my_list)
    

class Sales:
    def __init__(self, amount):
        self.amount = amount


def find_total(sales_list): #this function is not a part of sales class
    total = 0
    # here we created a local variable total for this function
    for sale in sales_list:
        print("New sale ...")
        print(sale.amount)
        total += sale.amount
    return total

# lets create a list which contains the sales objects
january_sales = [Sales(10), Sales(20), Sales(30)]
# inside tgis list we have automatically created 3 objects of the class Sales with values 10, 20 and 30
# now we will pass this list to the function find_total
total = find_total(january_sales)
print("total :", total)
# this will print 60
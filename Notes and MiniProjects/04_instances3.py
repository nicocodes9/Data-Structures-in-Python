class Circle :
    def __init__(self,  color, radius=4): #declaring it here means that if i dont pass a value to radius as an argument use 5 as a default
        self.radius = radius
        self.color = color


my_circle= Circle("blue") 
print(my_circle.radius)
# while declaring a default parameter we shouldn't spaces around the = sign 
# Yes: def __init__(self, name, age=10): ///Right
# No: def __init__(self, name, age = 10): ///wrong

#*********** the default value parameter should be the last parameter in the list of parameters

# otherwise there will be an error
# this rule is made so that we if we dont want to change the default value for an
#  instance , we can leave it as the last parameter and the rest of the parameters can be assigned easily 
my_another_circle = Circle("Green") # here i let the default value for the 
overwritten_circle = Circle("Green" , 9) #if we pass the value here it will overwrite the default value for this instance

print(overwritten_circle.radius) # prints 9
print(my_another_circle.radius) # prints 4

# loops in python
name ="John Doe"
for i in name:
    print(i) # prints each character in the string

# for loops in lists [arrays are called lists in python]
fruits = ["apple", "mango", "banana", "guava", "pear"]
for fruit in fruits:
    print(fruit) # prints each fruit in the list
    # we can also use the index of the list to print the fruits
    for i in fruit:
        print(i) # prints each character in the a single  fruit string


# range in python
# range is used to generate a sequence of numbers
# it is used in for loops to loop over a sequence of numbers
# it is used to generate a sequence of numbers from 0 to n-1
# it is used to generate a sequence of numbers from m to n-1

for k in range(5):  #means range should be less than 5
    print(k) # prints 0,1,2,3,4
    # print(k+1) that will print from 1 to 5


for h in range(2 , 6):
    print(h) # prints 2,3,4,5


# 3 parameters in range function
# start, stop, step
# start is the starting number of the sequence
# stop is the ending number of the sequence
# step is the difference between each number in the sequence , the interval to skip
# if we dont specify the step it will be 1 by default
for i in range(1, 10, 2):
    print(i) # prints 1,3,5,7,9
    # all odd numbers

# we can also update instances attributes later
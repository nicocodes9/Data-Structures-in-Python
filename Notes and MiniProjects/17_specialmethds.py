# the special methods ar easo referred as magic methods or dunder methods
# they are the methods that start and end with double underscore
# they are used to implement the behavior of the objects in python
# examples of special methods
# __len__ : to get the length of the object
# __str__ : to get the string representation of the object
# __repr__ : to get the official string representation of the object
# __add__ : to add two objects
# __sub__ : to subtract two objects
# __mul__ : to multiply two objects
# __truediv__ : to divide two objects
# __floordiv__ : to floor divide two objects
# __mod__ : to get the modulus of two objects
# __pow__ : to get the power of two objects
# __eq__ : to check if two objects are equal
# __ne__ : to check if two objects are not equal
# __lt__ : to check if one object is less than the other
# __le__ : to check if one object is less than or equal to the other
# __gt__ : to check if one object is greater than the other
# __ge__ : to check if one object is greater than or equal to the other
# __getitem__ : to get the item of the object
# __setitem__ : to set the item of the object
# __delitem__ : to delete the item of the object
# __iter__ : to iterate over the object
# __next__ : to get the next item of the object (this and iter are both used in loops behind the scenes)
# __contains__ : to check if the object contains the item
# __call__ : to call the object as a function
# __enter__ : to enter the context manager
# __exit__ : to exit the context manager

# how to use them
my_string = "hello world"
print(my_string.__len__()) # 11
print(my_string.__str__()) # hello world
print(my_string.__repr__()) # 'hello world'
print(my_string.__add__("!")) # hello world!
print(my_string.__mul__(2)) # hello worldhello world

class BankAccount:
    def __init__(self, owner , number, balance):
        self.owner = owner
        self.number = number
        self.balance = balance


    def make_deposit(self, amount):
        self.balance = self.balance + amount


    def make_withdrawal(self , ammount):
        if self.balance >= ammount:
            self.balance = self.balance - ammount
        else:
            print("the Account has insufficient balance to make this withdrawal")

    def __bool__(self):
        return self.balance > 0
    # now this will return the bool method true only when the balance in the account is greater than zero (positive)


myAccount = BankAccount("John Doe", "123456789", 1000)
print(bool(myAccount)) # True (by default the __bool__ method returns True)
# if we set the account balance to 0 the bool special method will return false

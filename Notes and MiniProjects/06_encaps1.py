class Car:

    def __init__(self, brand , model , year):
        self.brand = brand
        self.model = model
        self._year = year  # now this has become a protected attribute


my_car = Car("Porche", "911 Carerra", "2024")
print(my_car._year)
# we can easily edit the values in of year of the class outside of the class , to prevent this we can restrict acces to change values im this class
my_car._year = 8765
# we are able to do this because this attribute is public by nature
print(my_car._year)
# now the public elements of the class can be accessed easily outsidde of the class
# to prtect them from unauthorized acces and to protect them we make the non-public (not private)
# to make it non public we add an underscore to the attribute to make it protected

# python has no access modifiers like those public and private in Java and Cpp
# so we use to anme a variable differently to remind Devs that the variable shouldn't be accessed outside of the class

# technically that variable can still be accessed outside of the class if we also use the _ underscore with its name while accessing it
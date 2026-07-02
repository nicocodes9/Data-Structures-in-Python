# class attributes are the ones which belong to the class hence changing them affects all the instances
# class attributes are written and defined before the init method in the class
class Car:
    wheels = 4  # class attribute
    # we dont need to add  self here because its not the instance attribute it is a class attribute
    def __init__(self, brand, model, year):
        self.brand = brand  # instance attribute
        self.model = model  # instance attribute
        self.year = year  # instance attribute


# we can access the class attributes outside the class using the dot notation
print(Car.wheels)  # output: 4

# same sane be done inside of the class
class Movie:
    id_count = 1

    def __init__(self, title, year):
        self.title = title
        self.year = year
        self.id = Movie.id_count # we didn't defined the id at the parameters of this init methods , yet we can define this by using the reference of attribute from the class
        Movie.id_count += 1 # we are incrementing the id_count attribute of the class by 1 for each instance


my_movie = Movie("Casino Royale", 2006)
your_movie = Movie("Skyfall", 2012)
print(my_movie.id)  # output: 1
print(your_movie.id)  # output: 2

class Backpack:
    max_items =10

    def __init__(self):
        self.items = []


my_backpack = Backpack()
your_backpack = Backpack()

print(my_backpack.max_items)# output: 10
print(your_backpack.max_items)# output: 10
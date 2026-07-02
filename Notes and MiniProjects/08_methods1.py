class Circle:
    def __init__(self, radius):
        self.radius = radius

    def find_area(self):
        return 3.14 * self.radius * self.radius

    def find_perimeter(self):
        return 2 * 3.14 * self.radius
    
    def find_diameter(self):
        return 2 * self.radius
    
mycircle = Circle(5)
print(mycircle.find_area())
# method name should contain an underscore in python
print(mycircle.find_diameter())
print(mycircle.find_perimeter())


# example of calling methods by using a list

my_list = [1, 2, 3, 4, 5]
print(my_list.append(6)) # adds 6 to the end of the list
print(my_list)
print(my_list.pop()) # removes the last element
print(my_list)
print(my_list.insert(2, 7)) # inserts 7 at index 2
print(my_list)
print(my_list.remove(7)) # removes the first occurence of 7 from the list
print(my_list)
my_list.reverse() # reverses the list
print(my_list)
my_list.sort() # sorts the list
print(my_list)
my_list.clear() # clears the list
print(my_list)


class Backpack:
    def __init__(self):
        self.items = []

    def add_item(self, item): 
        if isinstance(item, str):
            self.items.append(item)
        else:
            print("Invalid item")

    def take_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return 1
        else:
            return 0

    def dump(self):
        self.items = []

    def has_item(self, item):
        if item in self.items:
            return 1
        else:
            return 0


mybag = Backpack()
mybag.add_item("book")
mybag.add_item("laptop")
mybag.add_item("pen")
mybag.add_item("water bottle")
mybag.add_item("notebook")
print(mybag.items)
print(mybag.has_item("book"))
print(mybag.has_item("phone"))
mybag.take_item("book")
print(mybag.items)
mybag.dump()
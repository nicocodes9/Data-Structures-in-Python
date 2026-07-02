class Player:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def move_up(self , change = 5):
        # here we have useda default argument incase the user does not provide a value
        self.y += change
    
    def move_down(self , change = 5):
        self.y -=change

    def move_left(self , change = 2):
        self.x -= change

    def move_right(self , change = 2):
        self.x += change

Player1 = Player(0,0)
print(Player1.x , Player1.y)
Player1.move_up()
print(Player1.x , Player1.y)
Player1.move_down()
Player1.move_left()
Player1.move_right()
print(Player1.x , Player1.y)
# calling method with argument
Player1.move_up(10)
print(Player1.x , Player1.y)


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
# using a default argument to print the unsorted list of items if the user does not provide sort condition
    def show_items(self , sort = False):
        if sort:
            self.items.sort()
            print(self.items)
        else:
            print(self.items)


# making another method to add multiple items in backpack at once . this will include calling another method inside a method
    def add_multiple_items(self , items):
        # using a for loop to iterate over the list of items and calling the add_item method to add each item in the backpack
        for item in items:
            self.add_item(item)


my_backpace = Backpack()
my_backpace.add_item("book")
my_backpace.add_item("laptop")
my_backpace.add_item("pen")
my_backpace.add_item("water bottle")
my_backpace.add_item("candy")

my_backpace.show_items() 
#this will ptrint the unsorted list of items as the user did not provide a sort condition
my_backpace.show_items(True)
# this will print the sorted list of items as the user provided a sort condition      

# lets clear the backpack items list
my_backpace.items.clear()  
my_backpace.add_multiple_items(["book" , "phone" , "clothes" , "food" , "sleeping bag"])
my_backpace.show_items(True)
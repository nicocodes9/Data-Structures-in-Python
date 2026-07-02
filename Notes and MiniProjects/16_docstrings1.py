# docstrings in python are used to document the code and provide information about the function, class, or module. They are written in triple quotes and can be accessed using the __doc__ attribute.
# docstrings are used to provide information about the function, class, or module. They are written in triple quotes and can be accessed using the __doc__ attribute.
# unlike comments, docstrings are not ignored by the interpreter and can be accessed at runtime. They are used to provide information about the function, class, or module. They are written in triple quotes and can be accessed using the __doc__ attribute.
# docstrings are used to provide information about the function, class, or module. They are written in triple quotes and can be accessed using the __doc__ attribute.

# example
def add(x, y):
    """
    This function adds two numbers and returns the result.
    :param x: first number
    :param y: second number
    :return: sum of x and y
    """
    return x + y
# note : type docstring should be immediately after the function definition and should be indented to the same level as the function body.
# there shouldn't be any blank lines between the function definition and the docstring.
# the docstring should be in triple quotes and should be indented to the same level as the function body.


a = 4
b = 5
result = add(a, b)
print(f"The sum of {a} and {b} is {result}")
print("Function docstring:", add.__doc__)
# while writting a multiline docstring we should indent the whole docstring to the same level as the function body.
# the docstring should be in triple quotes and should be indented to the same level as the function body.

#  in class we can also add docstrings for class documentations
# class docstring should be immediately after the class definition and should be indented to the same level as the class body.
class Backpack:
    """
    This class represents a backpack.
    It has a capacity and can hold items.
    """
    def __init__(self, capacity):
        """
        This function initializes the backpack with a given capacity.
        :param capacity: maximum capacity of the backpack
        """
        self.capacity = capacity
        self.items = []

    def add_item(self, item):
        """
        This function adds an item to the backpack.
        :param item: item to be added to the backpack
        """
        if len(self.items) < self.capacity:
            self.items.append(item)
            print(f"Added {item} to the backpack.")
        else:
            print("Backpack is full!")

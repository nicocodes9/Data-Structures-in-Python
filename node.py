class Node:
    """A class representing a node in a linked list.
    Each node contains a value and a reference to the next node in the list.
    """
    def __init__(self, value, next_node=None):
        self._value = value  # Use a private attribute
        self._next_node = next_node  # Use a private attribute for consistency

    @property
    def value(self):
        return self._value  # Return the private attribute
    
    @value.setter
    def value(self, value):
        self._value = value  # Set the private attribute

    @property
    def next_node(self):
        return self._next_node  # Return the private attribute
    
    @next_node.setter
    def next_node(self, next_node):
        self._next_node = next_node  # Set the private attribute

from node import Node


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_node(self, value):
        """Insert a new node with the given value at the end of the linked list."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif value <= self.head.value:
            new_node.next_node = self.head
            self.head = new_node
# defining insertion of nodeein the middle of the linked list
        else:
            previous = self.head
            runner = self.head.next_node
            while runner is not None and (runner.value < value):
                previous = runner
                runner = runner.next_node
            new_node.next_node = runner
            previous.next_node = new_node

    def print_list_items(self):
        if self.head is None:
            print("The list is empty.")
        else: 
            current = self.head
            while current is not None:
                print(current.value, end=" -> ")
                current = current.next_node
            print("None")

    def count_no_of_nodes(self):
        """Count the number of nodes in the linked list."""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next_node
        return count
    # there is also a recurcive way to count the number of nodes in the linked list

    def find_node(self, value):
        """Find a node with the given value in the linked list."""
        current = self.head
        while current is not None:
            if current.value == value:
                print("Node found with value!")
                return current
            current = current.next_node
        return None
    
    def delete_node(self, value):
        """Delete a node with the given value from the linked list."""
        if self.head is None:
            print("The list is empty.")
            return

        # If the node to be deleted is the head node
        if self.head.value == value:
            self.head = self.head.next_node
            return

        current = self.head
        while current.next_node is not None:
            if current.next_node.value == value:
                current.next_node = current.next_node.next_node
                return
            current = current.next_node
        print(f"Node with value {value} not found.")
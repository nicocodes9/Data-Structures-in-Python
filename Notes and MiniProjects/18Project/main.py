from node import Node
from linked_list import LinkedList

# node1 = Node(11)
# node2 = Node(22)
# node3 = Node(33)
# node1.next_node = node2
# node2.next_node = node3
# node3.next_node = None

# print(node1.value)  # Output: 11
# print(node1.next_node.value)  # Output: 22
# print(node1.next_node.next_node.value)  # Output: 33
# print(node1.next_node.next_node.next_node)  # Output: None

my_linked_list = LinkedList()
my_linked_list.insert_node(10)
my_linked_list.insert_node(20)
my_linked_list.insert_node(30)
my_linked_list.insert_node(25)
my_linked_list.insert_node(33)

print("Linked List after inserting nodes:")
# print(my_linked_list.head.value)  # Output: 10
# print(my_linked_list.head.next_node.value)  # Output: 20
# print(my_linked_list.head.next_node.next_node.value)  # Output: 25
# print(my_linked_list.head.next_node.next_node.next_node.value)  # Output: 30
# print(my_linked_list.head.next_node.next_node.next_node.next_node.value)  # Output: 33
# print(my_linked_list.head.next_node.next_node.next_node.next_node.next_node)  # Output: None
print(my_linked_list.print_list_items())  # Output: 10 -> 20 -> 25 -> 30 -> 33 -> None
print("Number of nodes in the linked list:", my_linked_list.count_no_of_nodes())  # Output: 5
print("Finding node with value 25:")  
print( my_linked_list.find_node(25).value)  # Output: 25
# deleting node with value 25
print("Deleting node with value 25:")
my_linked_list.delete_node(25)  # Output: Node with value 25 deleted.
print("Linked List after deleting node with value 25:")
print(my_linked_list.print_list_items())  # Output: 10 -> 20 -> 30 -> 33 -> None
# if we delete a value that is not in the list
my_linked_list.delete_node(50)  # Output: Node with value 50 not found.
# deleting the last node
print("Deleting the last node with value 33:")
my_linked_list.delete_node(33)  # Output: Node with value 33 deleted.
print("Linked List after deleting the last node:")
print(my_linked_list.print_list_items())  # Output: 10 -> 20 -> 30 -> None


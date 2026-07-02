from node import Node

node1 = Node(11)
node2 = Node(22)
node3 = Node(33)
node1.next_node = node2
node2.next_node = node3
node3.next_node = None

print(node1.value)  # Output: 11
print(node1.next_node.value)  # Output: 22
print(node1.next_node.next_node.value)  # Output: 33
print(node1.next_node.next_node.next_node)  # Output: None
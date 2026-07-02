# mutables are the objects in python which can be modified / altered after creation
# list, dictionaries, set are the examples of mutables

# while immutable objects are the objects in python which can not be modified / altered after creation
# booleans , int, float, string, tuple are the examples of immutables

def absolute_value(seq):
    for i in range(len(seq)):
        seq[i] = abs(seq[i])
    return seq

sequence = [-1, 2, -3, 4, -5]
print(absolute_value(sequence))
print(sequence) # the original list is also modified

# working with tuples
def absolute_value(seq):
    seq = list(seq)
    for i in range(len(seq)):
        seq[i] = abs(seq[i])
    return tuple(seq)

seq = (-1, 2, -3, 4, -5)
print (id(seq))
new_seq = absolute_value(seq)
print(new_seq) # the new tuple
print (id(new_seq)) # the id of the tuple
print(seq) # the original tuple is not modified
print (id(new_seq)) # the id of the tuple
# this will be different than the id before the function call
# this is because the tuple is immutable and a new tuple is created
# and the reference
# of the new tuple is returned by the function

# tuple is immutable but if we try to modify an object inside the tuple it becomes mutable
# and the original tuple is not modified
# this is the reason why we are able to modify the list inside the tuple but not the tuple itself

# cloning of objects in python 
a = [1 ,2 ,3 ,4]
b = a[:]
b[0] = 34
print(b)
print(a)
# thus the orignal object a is unaffected by the modification in b because of cloning and the clone object is independent of the original object
# this is shallow copy of the object

# cloned touples have the same id as the original tuple
# this is because the tuple is immutable and the id of the tuple is not changed when we clone it
# and the reference of the original tuple is returned by the function
# but cloned lists have different id as the original list
# this is because the list is mutable and the id of the list is changed when we clone it
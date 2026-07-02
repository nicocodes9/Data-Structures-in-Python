class Backpack :
    def __init__(self):
        self.items = ["pencils", "pens", "books", "notes" ]


n_backpack = Backpack()
print(n_backpack.items)  # Output: ['pencils', 'pens', 'books' , 'notes']
n_backpack.items = ["scales", "ink", "laptop"]
print(n_backpack.items)  # Output: ['scales', 'ink', 'laptop']
# we can only edit a list with list

# deleting an attribute from an instance
# we can delete an attribute from an instance using the del keyword

del n_backpack.items
# print(n_backpack.items) this will throe an error coz the attribute is deleted

# creating an example bacteria class 
class Bacteria:
    def __init__(self, name, shape, size, organelle):
        self.name = name
        self.shape = shape
        self.size = size
        self.organelle = organelle
        print(name)
        print(shape)
        print(f"size : {size} micro meter")     
        #these statements can print both string and defined attributes with using a single print statement 
        print(f"organelles present : {organelle}")


E_coli = Bacteria ("Escherichia Coli", "rod shaped (Bacillus)" , 2 ,["membrane" , "ribosomes", "plasma", "Nucleoid" ] )
S_aureus = Bacteria ("Staphylococcus aureus", "spherical (Coccus)" , 1 ,[ "ribosomes", "Cell wall", "Capsule" ] )
B_subtilis = Bacteria ("Bacillus Subtilis", "rod shaped (Bacillus)" , 4 ,["Flagella" , "Capsule", "Cell Wall", "Endospores" ] )

# print(E_coli)
# print(S_aureus)
# print(B_subtilis)


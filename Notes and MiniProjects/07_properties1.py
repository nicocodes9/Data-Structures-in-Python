class Movie:
    def __init__(self, title, rating):
        self._title = title
        self._rating = rating
        # defining get method
    
    def get_title(self):
        return self._title
    def get_rating(self):
        return self._rating
    

My_movie = Movie("Skyfall" , 4.6)
print(My_movie.get_title())
print(My_movie.get_rating())

class Dog:
    def __init__(self, name, age ):
        self._name = name
        self.age = age
        # defining set method

    def set_name(self, new_name):
        # now to set the name we will use the set method
        # it will allow us to validate the new_name before we assign it to the name attribute
        if isinstance(new_name, str) and new_name.isalpha():
            # here we are validating that if the new name is a string and is alphabetical only then we will assign it to the name attribute
            self._name = new_name
        else:
            print("Invalid name. Please enter a string with only alphabets.")


My_dog = Dog("Tony", 4)
print("My Dog's name is ", My_dog._name)
My_dog.set_name("Tommy")
print("After remnaming, now his name is ", My_dog._name)

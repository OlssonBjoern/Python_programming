
# Basic class definitions

# TODO : Create a basic class
class Book:
    # init-function is a function that when the class is created, the 
    # init function is called to initialize that object with information
    def __init__ (self, title):
        self.title = title


# TODO : create instance of class
# Or construct the object
book1 = Book("Shantaram")
book2 = Book("Dracula")


# TODO : print the class and property
print(book1)
print(book1.title)
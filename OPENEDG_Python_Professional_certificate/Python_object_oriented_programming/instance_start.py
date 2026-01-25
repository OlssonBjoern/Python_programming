
# Using instance methods and attributes

# TODO : Create a basic class
class Book:

    # init-function is a function that when the class is created, the 
    # init function is called to initialize that object with information
    def __init__ (self, title, author, pages, price):
        self.title = title
        # TODO : add properties
        self.author = author
        self.price = price
        self.pages = pages
        self.__secret = "This is a secret attribute"

    # TODO : create instance methods
    # Every instance method takes an object as the first parameter

    def getprice(self):
        # The use of hasattr() checks if the attribute exists since in this case the discount MIGHT exist
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
        
        return self.price
    
    # Set discount
    # _discount means that this can't be relied on since it has the _ before discount
    def setdiscount(self, amount):
        self._discount = amount

# TODO : create instance of class
# Or construct the object
book1 = Book("Shantaram", "Gregory David Roberts", 1049, 149 )
book2 = Book("Dracula", "Bram Stoker", 321, 100)


# TODO : print the class and property
print(book1.title)

print(book1.getprice())

# Testing setting a discount
book2.setdiscount(0.10)
print(book2.getprice())

print(book2.__secret)
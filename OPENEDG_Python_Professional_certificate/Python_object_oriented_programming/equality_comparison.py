
# Using __eq__ , __ge__ , __lt__


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    
    # __eq__ checks for equality between two objects
    def __eq__(self, value):

        # Check if all values in the objects are the same
        # isinstance() checks if the value we compare with is of type: object Book
        if not isinstance(value, Book):
            raise ValueError("Can't compare book object to non-book object")
        
        return (self.title == value.title and
                self.author == value.author and
                self.price == value.price)

    # __ge__ establishes >= relationship with another obj
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book object to non-book object")
        return self.price >= value.price
    
    # __lt__ establishes < relationship with another obj
    # Here we check if the price is less than
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book object to non-book object")
        return self.price < value.price   



b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("Dracula", "Bram Stoker", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("C++ a beginner's guide", "Herbert Schildt", 19.98)

print(b1==b3)
print(b1==b2)
# Will create an error message
##print(b1 == 42)

# Try to check if b2 is >= b1
print(b2 >= b1)
print(b2 < b1)

# Sorting the books
books = [b1, b3, b4, b2]
books.sort()
print([book.title for book in books])
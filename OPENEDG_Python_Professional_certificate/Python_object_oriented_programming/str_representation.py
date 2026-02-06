
# Using "magic methods" __str__ to make string representation of objects, usually intended to be shown to the user
# __repr__ is made to recreate the object in its current state


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # use __str__ to return a string
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # use __repr__to return an object representation
    # repr is usually used in debugging and should at least be used for this purpose
    def __repr__(self):
        return f"title={self.title}, author={self.author}, price={self.price}"

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("Dracula", "Bram Stoker", 29.95)

print(b1)
print(b2)
print(str(b1))
print(repr(b2))
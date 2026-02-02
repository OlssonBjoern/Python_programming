# Inheritance between classes

class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

# Inherits Publication and starts a new sub-super-class for periodical information
class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher

class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages

# Magazine inherits Periodical which inherits Publication
class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)

# Newspaper inherits Periodical which inherits Publication
class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)

b1 = Book("Dracula", "Bram Stoker", 357, 29.90)

print(f"{b1.author}s {b1.title} is {b1.pages} long and costs {b1.price}$")
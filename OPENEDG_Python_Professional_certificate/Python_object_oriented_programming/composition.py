# Composition
# When we create objects that consists of objects
# e.g Books could be one object and Author could be another object.


class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price

        self.author = author

        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append((chapter))
    
    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        return result


class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.fname} {self.lname}"
    

class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount


auth = Author("Herbert", "Schildt")
b1 = Book("C++ A beginners guide", 299.99, auth)

b1.addchapter(Chapter("Chapter 1 - C++ Fundamentals", 40))
b1.addchapter(Chapter("Chapter 2 - Introducing Data Types and Operators", 34))
b1.addchapter(Chapter("Chapter 3 - Program Control Statements", 38))

print(b1.title)
print(b1.author)
print(b1.getbookpagecount())
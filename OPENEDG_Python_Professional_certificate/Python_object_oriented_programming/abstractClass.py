# Using abstract base classes to enforce class constraints

# Abstract classes are classes that needs to be enforced to sub-classes
# Like below making the calcArea and JSONify something that each other class has to implement


from abc import ABC, abstractmethod

class GraphicShape(ABC):
    def __init__(self,):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass

class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius
    
    # Calculate area of circle
    def calcArea(self):
        return 3.14 * (self.radius ** 2)
    
    def toJSON(self):
        return f"{{'Circle': {str(self.calcArea())}}}"



class Square(GraphicShape):
    def __init__(self, side):
        self.side = side
    
    def calcArea(self):
        return self.side * self.side

c = Circle(10)
print(c.calcArea())

print(c.toJSON())
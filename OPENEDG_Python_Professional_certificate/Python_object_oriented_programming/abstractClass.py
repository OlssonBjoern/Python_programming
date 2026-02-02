# Using abstract base classes to enforce class constraints


class GraphicShape:
    def __init__(self,):
        super().__init__()

    def calcArea(self):
        pass



class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius


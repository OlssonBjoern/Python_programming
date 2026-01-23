# Checking what type or class an object has

class SuperheroDC:
    def __init__(self, alias):
        self.alias = alias


class SuperheroMarvel:
    def __init__(self, name):
        self.name = name

# Instance creation of classes

dcHero1 = SuperheroDC("Batman")
dcHero2 = SuperheroDC("Aquaman")
marvelHero1 = SuperheroMarvel("Tony Stark")
marvelHero2 = SuperheroMarvel("King T\'Challa")

# Use the type()

print(type(dcHero1))
print(type(marvelHero1))
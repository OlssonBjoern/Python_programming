
# Working with class-level and static methods and members


class Hero:

    # Properties defined at the class level are shared by all instances
    # So for example you could have that all heroes has strength as a power for example
    HERO_TYPES = ("Human", "Alien", "Mutant")


    # Creating a property that isn't available to other classes
    __herolist = None

    # TODO : Creating a class method
    @classmethod
    def get_hero_types(cls):
        return cls.HERO_TYPES

    # Creating a static method
    def getherolist():
        if Hero.__herolist == None:
            Hero.__herolist = []
        return Hero.__herolist

    # Instance method that sets the heroes name
    def set_alias(self, newAlias):
        self.alias = newAlias

    def __init__(self, alias, herotype):
        self.alias = alias
        if (not herotype in Hero.HERO_TYPES):
            raise ValueError(f"{herotype} is not a valid hero type")
        else:
            self.herotype = herotype


print("Hero types: ", Hero.get_hero_types())

h1 = Hero("Hero1", "Human")
h2 = Hero("Hero2", "Alien")

# User static method to acces singleton object
theheroes = Hero.getherolist()
theheroes.append(h1)
theheroes.append(h2)
print(theheroes)
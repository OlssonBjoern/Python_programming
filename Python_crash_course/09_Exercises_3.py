# Exercises with classes regarding inheritance

# 9.6 Ice Cream Stand

class Restaurant:

    def __init__(self, restaurant_name, cuisine):
        self.restaurant_name = restaurant_name
        self.cuisine = cuisine
        
    def restaurant_open(self):
        reservation_time = int(input("At what time do you want your reservation? "))

        if reservation_time >= 23 and reservation_time < 10:
            print("We are sorry, the restaurant is not open at this hour")
        else:
            print(f"Great, your reservation is made for {reservation_time} o'clock, we hope to see you then!")

    def describe_restaurant(self):
        print(f"This restaurant serves {self.cuisine}.")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine, flavours):
        super().__init__(restaurant_name, cuisine)
        self.flavours = flavours

    def displayFlavours(self):
        print("Current flavours to chose from: ")
        for flavour in self.flavours:
            print(flavour)

stand = IceCreamStand("Boms", "Ice cream", ["Strawberry", "Vanilla", "Pistachio"])

stand.displayFlavours()


# 9.7 Admin
# Extension of old User class, should have privileges attribute and a method called "show_privileges()"

class User:

    def __init__(self, name, role, userId):
        self.name = name
        self.role = role
        self.userId = userId
    


class Admin(User):

    def __init__(self, name, role, userId, privileges):
        super().__init__(name, role, userId)
        self.privileges = privileges

    def show_privileges(self):
        print(f"{self.name} works in {self.role} with ID: {self.userId} and has admin level: {self.privileges[1]}")


ad = Admin("Steve Jobs", "Idiot branch", 3, ["can post", "full privileges", "can't do shit"])

ad.show_privileges()

# 9.8 Privileges
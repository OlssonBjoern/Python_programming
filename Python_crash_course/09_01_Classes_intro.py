
class Dog:

    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age

    def sit(self):
        print(f'{self.name} is sitting')

    def presentation(self):
        print(f'{self.name} is {self.age} years old and a beautiful {self.type}!')

    def roll_over(self):
        print(f'{self.name} is rolling over, good for a {self.age} year old dog')

# Instantiate class object

my_dog = Dog("Zach", "Rotweiler", 2)

my_dog.presentation()

my_dog.roll_over()

# ----------------------------- Exercises for first section ------------------------------------- #

class Restaurant:
    
    # 9.1 Create the restaurant class with the name and cuisine attributes and two methods

    def __init__(self, restaurant_name, cuisine):
        self.restaurant_name = restaurant_name
        self.cuisine = cuisine

    def restaurant_open(self):
        print(f"{self.restaurant_name} is open between 08:00 and 23:00 every day!")

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a fine restaurant in the Gamla Stan district of Stockholm that serves {self.cuisine} as their main cuisine!")
    
    # 9.2 Create three restaurants

first_restaurant = Restaurant("Franzén", "Italian")

first_restaurant.describe_restaurant()

second_restaurant = Restaurant("Liffey", "Pub food")

second_restaurant.describe_restaurant()

third_restaurant = Restaurant("Gondolen", "French")

third_restaurant.describe_restaurant()

# 9.3 
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


# 9.7 Admin

# 9.8 Privileges
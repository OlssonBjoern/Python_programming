
class Restaurant:

    def __init__(self, name):
        self.numbers_served = 0

    def set_numbers_served(self, amount_of_customers):

        self.numbers_served = amount_of_customers
        print(f"Current amount of customers served are: {self.numbers_served}")

    def increment_served(self, added_customers):
        self.numbers_served += added_customers
        print(f"A hopefully updated number: {self.numbers_served}")


rest1 = Restaurant("Scarpetta")

rest1.set_numbers_served(10)

rest1.increment_served(5)



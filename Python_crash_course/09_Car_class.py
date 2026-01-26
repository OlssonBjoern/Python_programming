
class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # Adding a default value to the odometer reading
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    # Adding method to update the odometer reading
    def update_odometer_reading(self):

        mileage = int(input("Enter the cars current odometer reading: "))

        self.odometer_reading = mileage

        if mileage >= self.odometer_reading:
            print(f"This car has an updated odometer reading of: {mileage}")
        else:
            print("You can't roll back the odometer reading!!")
    

my_new_car = Car('Volkswagen', 'Multivan', 2022)

print(my_new_car.get_descriptive_name())
my_new_car.update_odometer_reading()

# Adding Electric car class to practice inheritance
# This class should only add stuff specific to electric cars and not general things like the Car class already implemented

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # Adding an attribute to the Electric car class only
        self.battery_size = 75

    def describe_battery(self):
        print(f"The battery for this {self.model} is a {self.battery_size}-kWh one")

my_kia = ElectricCar('kia', 'ev3', '2020')
print(my_kia.get_descriptive_name())
my_kia.describe_battery()


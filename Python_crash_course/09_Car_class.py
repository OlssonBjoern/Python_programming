
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
    def update_odometer_reading(self, mileage):
        self.odometer_reading = mileage

        if mileage >= self.odometer_reading:
            print(f"This car has an updated odometer reading of: {mileage}")
        else:
            print("You can't roll back the odometer reading!!")
    

my_new_car = Car('Volkswagen', 'Multivan', 2022)

print(my_new_car.get_descriptive_name())
my_new_car.update_odometer_reading(24)
my_new_car.update_odometer_reading()
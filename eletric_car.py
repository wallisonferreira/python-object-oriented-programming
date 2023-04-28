from car import Car

class EletricCar(Car):
    
    def __init__(self, make, model, year, max_speed, battery_size):
        super().__init__(make, model, year, max_speed)
        self.battery_size = battery_size

    def charge(self):
        print("Charging the battery...")

my_car = EletricCar("Tesla", "Model S", 2022, 150,  '100 kWh')
my_car.charge()

# print(my_car.get_speed())
# my_car.increase_speed(20)
# print(my_car.get_speed())
# my_car.increase_speed(50)
# print(my_car.get_speed())
# my_car.increase_speed(50)
# print(my_car.get_speed())
# my_car.increase_speed(100)
# print(my_car.get_speed())
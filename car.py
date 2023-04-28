from vehicle import Vehicle

class Car(Vehicle):

    def __init__(
            self, 
            make, 
            model, 
            year, 
            max_speed = 100):

        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.__speed = 0
    
    def honk(self):
        print("Honk honk!")

    def increase_speed(self, speed):
        self.__accelerate(speed)

    def get_speed(self):
        return self.__speed

    def __accelerate(self, speed):
        if self.__speed + speed <= self.max_speed:
            self.__speed += speed
        else:
            self.__speed = self.max_speed
    
    def start_engine(self):
        print("Starting the car's engine...")
        #return super().start_engine()
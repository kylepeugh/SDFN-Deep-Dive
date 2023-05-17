# inheritance is used to build a new class based on
# an existing class
class Car:
    def __init__(self, color):
        self.color = color
        print("Hello, " + self.color + " car!")
        print(self)
# let's create two instances of the car class
red_car = Car("red")
black_car = Car("black")

# to use inheritance, you should pass the parent class name
# as a parameter in the child class
class Electric_car(Car):
    def model(self, model):
        self.model = model
        print("This is an electric car from " + self.model)
# let's create two instances from the Elect_car class
elect_car = Electric_car("green")
elect_car01 = Electric_car("blue")
# now, check if the red and black cars are instances of the Car class
print(isinstance(red_car, Car))
print(isinstance(black_car, Car))
print(isinstance(elect_car, Car))
print(isinstance(elect_car, Electric_car))
print(isinstance(elect_car01, Electric_car))
print(isinstance(red_car, Electric_car))
print(red_car.__dir__())
print(Electric_car.__dir__(elect_car))
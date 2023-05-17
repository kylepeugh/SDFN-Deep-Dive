# back to the previous example
class Car:
    def __init__(self, color):
        self.color = color
        print("Hello, " + self.color + " car!")
# create a-n instance of the Car class
red_car = Car("red")
class Electric_car(Car):
    def __init__(self, speed):
        self.speed = speed
    def model(self, model):
        self.model = model
        print("This is an electric car from " + self.model)

# if we create a new instance of the Elect_car
elect_car01 = Electric_car("red")
# As you can see this is not working, let's check the __dir__
print(elect_car01.__dir__())
# no color attribute is there, this is a result of using the __init__
# method inside the Elect_car class
# the child __init__ method will override the __init__ method of the parent
# to avoid this, the super() function is used like this
class Child_car(Car):
    def __init__(self, color, speed):
        super().__init__(color)
        self.speed = speed
# now, we can test this
new_child_car = Child_car("Red", 200)
print(new_child_car.__dir__())
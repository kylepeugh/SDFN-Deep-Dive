# the self parameter is used to refer to the object created by a class 
# let's explore that
class Car():
    # the __init__ method is used to initialize the object
    def __init__(self):
        #let's print the self paramater
        print(self)
# create a new instance
new_car = Car()
print(new_car.__dict__)
# let's add some attributes to the object
new_car.color = "red"
new_car.speed = 200
print(new_car.__dict__)
print(new_car.__dir__())
# the self parameter should be passed to each method 
# another example
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print(f"Hello, my name is {self.name}, and my age is {self.age}")
        
dog01 = Dog("lassy", 4)
dog02 = Dog("tommy", 9)
dog01.speak()
dog02.speak()
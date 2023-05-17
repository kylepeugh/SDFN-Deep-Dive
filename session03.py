# classes are used to create objects
# let's explore the syntax
class Test:
    # The __init__ method is a special method 
    # that initializes the object's attributes when it is created.
    # the self parameter have to be paased to the __init__ method
    def __init__(self):
        print(self)
    # declare a class level variable
    test_var = "this is a class level variable"
    # define a method to print this variable
    def output(self):
        print(self.test_var)
# to create a new object we call the class like a normal function
Test()
# As you can see the new object is created and
# Python iterpreter is giving us a reference to this object in the memory
# is there any way to see this object?
test01 = Test()
# using the dir built-in method we can explore
# the attributes and methods of an object in Python
print(test01.__dir__())
# As we haven't add any attributes or methods
# Python will output a list of built-in methods
# to see if we can add our own attributes and methods
# let's add some
# Now, we should see the test_var and output methods
# we can call the output method
test01.output()

# That's okay, now let's talk about instances
# we use classes to instantiate objects, which means
# create new objects from the same original attributes and methods with the 
# ability to modify or update these attributes and methods
# to test that, let's do create more than one instance of our test object
test02 = Test()  
test03 = Test()  
test04 = Test()
# As you can see, each object is stored in a different place in the memory
# To make sure, let's compare two of them
print(test01 == test02)
# this was evaluated to false which means each object is independent
# so, can we make some modifications??
test02.test_var = "this variable was modified!!!!"
print(test02.test_var)
# let's update it
test02.new_var = "this is a new variable related to test02"
print(test02.new_var)
# now, let's check the directory 
print(test02.__dir__())
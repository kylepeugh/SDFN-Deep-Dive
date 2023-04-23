# variables is a main concept in all programming languages
# No way to build any functionality unless you use a variable
# to declare a variable in Python, you may use this syntax
test = 'anything'
# variable is refering to a place on the memory where the value live
# when declaring a variable directly in your script it will be available for use anywhere
# that called the variable scope 
a = 2
b = 8
print(a + b)
# when we build a function, we can use the variable inside it
def sum(a, b):
    print(a + b)
sum(a, b)
# let's see what is happening if we change the values
def change():
    a = 80
    print(a)
# we call the function to see that it outputs the new value 80
change()
# now, let's print the value of a again 
print(a)
# the value of a is still 2, why is this happening?
# The scope of the variable is where the program can reach its value
# to fix this we should have a way to tell the Python interpreter to reach the global variable
# to do this we have to use a keyword called global
def change2():
    global a 
    print(a)
    a = a + 80
    print(a)
change2()
print(a)
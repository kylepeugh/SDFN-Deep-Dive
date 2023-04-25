# starting with the built-in modules
import math

print(math.pi)

# Another way is to name your module 
# while importing to reduce the typing effort
import random as R

menu = ['milk', 'tea', 'coffee']
print(R.choice(menu))

# to run the code type this command
# python session01.py

# As developers, we can build our own custom modules
# Using the same example, I will create another file 
# Instead of using the mouse, I will use this command in the terminal 
# touch custom-module.py
# I will copy the menu above to the new file
# Now the file has been created correctly and I can import it

# import custom-module 

# An error has occured because we just break the module naming convention in python 
# by adding a dash to separate the two words custom-module
# because Python treats dashes as a minus operator
# Also, the usage of underscors is discouraged  
# to fix this, I will change the name to be short all lowercase name
# Now, We can import it
import custom
# use it inside our script 
print(custom.menu)
# output >>> ['milk', 'tea', 'coffee']
# we can use the above example to get a random value
print(R.choice(custom.menu))

#_____________________ recap __________________________________
# Modules are used to organize our code to be easily reused 
# while building your script, if you feel that your program is growing
# you can think of collecting the related blocks into a custom module.




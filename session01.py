# in adventure game project, you are going to use strings and lists data types 
# strings are a sequence of characters like this
name = "John"
print(name)
# if we try the same syntax with single quotes, it will be correct 
# so, can you tell me why using single quotes?
# check this examples
# welcome = "we're glad to have you!"
# welcome02 = 'we're glad to have you'

# back to strings concatenation
string01 = "some text"
string02 = "new text"
# to keep a white space between the two strings, we add a " "
print(string01 + " " + string02)
# another easy way to achieve that is by using the f statemnet or the template literals
print(f"{string01} {string02}")
# if there are some names and we want to store them all at once, we need a list
names = ["John", "Elly", "Sam"]
print(names)

# to access a specific character in a string or a specific item in a list
# we use the character or the item index
# indexing is to count the characters or the items starting from 0, 1, 2, ...
# to access a character or an item, we use square brackets 
print(name[0], name[1], name[2], name[3])
print(names[0], names[1], names[2])

# another way is the negative indexing
print(name[-1], name[-2], name[-3], name[-4])
print(names[-1], names[-2], names[-3])

# Slicing is another way to access strings or lists
print(name[1:3])
print(names[1:3])

# changing a value at a specific index in a string
text = "text to change"
# text[0] = "n" # TypeError: 'str' object does not support item assignment
items = ["red", "green", "blue"]
items[0] = "black"
print(items)
# strings are immutable || lists are mutable

# built-in methods for strings
text02 = "TexT"
print(type(text02))
print(len(text02))
print(text02.lower())
print(text02.upper())

# built-in methods for lists
cars = ["BMW", "VW", "FORD"]
print(type(cars))
# the list length
print(len(cars))

# reverse the list
cars.reverse()
print(cars)

# add a new item at the end of a list
cars.append("HONDA")
print(cars)

# remove the last item in a list
cars.pop()
print(cars)

# insert an item before a specific index
cars.insert(0, "AUDI")
print(cars)

# Booleans is the logical True or False values 
# we can declare booleans directly or as a result of a comparison
a = True
b = 1 > 5
c = 5 > 1
print(a, b, c)

# some values are considered False by default in python
# False, None, zero, and empty sequence will always evaluate to False 

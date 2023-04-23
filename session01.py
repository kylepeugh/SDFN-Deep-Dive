# in adventure game project, you are going to use strings and lists data types 
# strings are a sequence of characters like this
name = "John"
print(name)

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
print(len(text02))
print(text02.lower())
print(text02.upper())

# built-in methods for lists
cars = ["BMW", "VW", "FORD"]
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
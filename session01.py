# Operators are special symbols that perform operations on variables and values.
# Arithmetic Operators in Python are used to acomplish the basic arithmetic operations
x = 10
z = 50
print(x + z)
print(x - z)
print(x * z)
print(x / z)
print(z % x)

# Assignment Operators 
# the single equal sign is used to assign a value to a varible
num = 15
num += 1 # num = num + 1
print(num)
num -= 5 # num = num - 5
print(num)
num *= 3 # num = num * 3
print(num)
num /= 3 # num = num / 3
print(num)

# Comparison Operators
# used to compare two variables or values
# the output is boolean
num01 = 10 
num02 = 5
print(num01 == num02)
print(num01 != num02)
print(num01 > num02)
print(num01 < num02)
print(num01 >= num02)
print(num01 <= num02)

# logical operators
# used to compin two or more comparisons 
# the output is boolean
print((num01 != num02) and (num01 > num02)) # true only if both true
print((num01 == num02) or (num01 > num02)) # true if one true
print(not num02) # true if operand is false
num03 = '' # False values in Python are empty strings or lists, 0, None and False
print(not num03) # true because the string is empty

# Membership operators

# used to check if a value or variable is found in a sequence
string01 = "Hello"
print("H" in string01)
print("e" not in string01)
list01 = ["item01", "item02", "item03"]
print("item01" in list01)
print("item1" not in list01)



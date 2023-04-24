# loops are used to execute a code block repeatedly
# check this syntax
# for i in 5:
#     print(i) # TypeError: 'int' object is not iterable
# for loops in Python do not iterate over integers
# the reference should be a sequence like lists or strings
# to fix the above code let's try a builtin function called range()
for i in range(5):
    print(i)
# using a string length as a reference
text = "hello"
for i in range(len(text)):
    print(i)
    print(text[i])
# using a for loop to iterate over the characters of a string
for i in text:
    print(i)
# using a list length as a reference
items = ["item01", "item02", "item03"]
for i in range(len(items)):
    print(i)
    print(items[i])
# using a for loop to iterate over the items of a list
for item in items:
    print(item)

# while loops are another way to execute code until a certain condition is true
# while 1 < 5:
#     print("working!")
# that's bad, we have mistakely create an infinite loop
# infinite loops are happening when the codition is always true
num = 8 
while num < 15:
    print(num)
    # a way to change the codition so the loop has an end
    num += 1

# using a for loop inside a function
def calc():
    students = ["john", "sam", "elly"] 
    for student in students:
        print("Hello, " + student)
    
calc()
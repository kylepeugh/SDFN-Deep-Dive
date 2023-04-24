# to start working with pycodestyle, install it using pip
# using this command in the terminal
# pip install pycodestyle
# you can check the version using this command
# pycodestyle --version
# to use it to check your own code, use this command
# pycodestyle <file_name.py>

# Indentation in Python is very important 
# 4 spaces is used to indent code blocks
# check this example

for i in range(5):
    # this line will be repeated
    print(i)
# this line will be executed for one time outside the for loop
print(i)

# line length should be shorter than 79 characters
# what to do if you have a long line? 
# check this approach
print("texttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttext")
print("texttexttexttexttexttexttext"
      "texttexttexttexttexttexttext"
      "texttexttexttexttexttexttext")

# Naming conventions in Python is to use snake_case not camelCase
# this is a snake_case 
first_student = "jane"
# this is a camelCase 
firstStudent = "jane"

# Whitespaces are important in Python, let's make it a habit
name="sam" # not right
name = "sam" # that's better
if name=="sam": # name == "sam"
    print("your name is "+name) # print("your name is " + name)

# comments are important as they documenting the development process 
# for future you and other developers to be able to understand your code blocks
# commenting a code block is a good practice to keep a piece of code inside 
# your script without affecting your program run
# to comment any code block in VSC, select the block, click ctrl + k + c
# to uncomment any code block in VSC, select the block, click ctrl + k + u



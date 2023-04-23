# functions  is a basic concept of any programming language
# function is a block of code built to acomplish a specific task
# check this pseudo code
'''
def <function_nam>():
    <code_to_be_exectued>
<function_name>()
'''
# a function consists of three parts
# 1. a function definition
def my_func():
# 2. indented code block to be executed
    print("my first function is working!")
# 3. a function call 
my_func()

# function is a reusable block of code
# check how can we build a function with reusability in mind
def sum(x, z):
    print(x + z)
# x and z are called function parameters an equivalent of ordinary variabls
# but to be used inside a function, when call a function we pass arguments 
# or real values we need the function to calculate
sum(50, 78)
sum(55, 54)
sum(150, 965)

# in the previous example, we printed the sum of x and z to but in some cases
# we need a more dvanced aproach to be able to use the calculated value 
# in other places in our program, not just print it
# to achieve this, we can use the return keyword as follows
def sum_return(a, b):
    return a + b
sum_return(2, 5) 
# not that nothing has been printed because we did not use the print function
# so, how is this going to help?
# we can use the result of this function as argument in the sum() function
sum(sum_return(4, 5), sum_return(8, 6))

# or storing them into variables like that
sum_num01 = sum_return(2, 10)
sum_num02 = sum_return(8, 1)
sum(sum_num01, sum_num02)
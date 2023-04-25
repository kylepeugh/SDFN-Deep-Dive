# as you may know, the Python interpreter is excuting any Python script in linear way
# line by line 
print("first..!")
print("second..!")
print("third..!")

# in some cases, we need to excute the code in another sequence
# conditionals are used to acomplish this
# if statement is used to excute a code block if a certain condition was met
# check this psuedo code
""" if <this_condition_is_true>:
        excute_this_code_block """

# note that two things are required in a conditional 
# 1. a colon at the end of the expression  (:)
# 2. an indented statement to be excuted.
# indentation is the way Python interpreter uses to execute a code block or a multiple lines of code 
num01 = 10
num02 = 5
if num01 > num02:
    # print(num01 + "is > " + num02) # as num01 & num02 are integers,  an error will occur
# how can we fix this error?
    print("That's correct!")
# note that any statement at the same level of indentation will be executed 
    # print("line two")
# in many cases, we need to execute something if the expression was false
# else statements are used to achieve that
else:
    print("that's wrong!")
# in some cases, more than one codition should be checked
# elif is the keyword used to achieve that
cond01 = "first..!"
cond02 = "second..!"
cond03 = "third..!"
if cond01 == "first..!":
    print(cond01)
if cond02 == "second..!":
    print(cond02)
if cond03 == "third..!" :
    print(cond03)
# check what happens if we use elif instead
if cond01 == "first..!":
    print(cond01) # if the first condition is true, next blocks are not going to be executed 
elif cond02 == "second..!":
    print(cond02)
elif cond03 == "third..!" :
    print(cond03)
# you may use a nested if statement like this
if cond01 == "first..!":
    if 20 > 10:
        print("nested if statement is working!")
# to achieve the same result you may combin the two conditions using logical operators
if cond01 == "first..!" and 20 > 10:
    print("compined if statement is working!")


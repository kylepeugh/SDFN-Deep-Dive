# 4. Make sure the player gives a valid input
# user_choice = input("choose 1 or 2\n 1. Water\n 2. Tea\n")
#     # now, to keep the game play easy and consistent, options should be like 1 or 2
#     # to check invalid input, you have to use a conditional like this3
# if user_choice == 1:
#     # a problem will rise here because of the differnt datatypes
#     # as we compare the string (user_choice) with the integer (1)
#     # to fix this, you can  use something like str or ""
#     print("your choice is 1")
    
# elif user_choice == "2":
#     print("your choice is 2")
# else:
#     print("this is an invalid input?!!!")
#     # if you test this with an invalid input, you can see the game will be terminated
#     # to avoid this, we have to ask the player again
#     user_choice = input("choose your drink 1. water 2. tea")
#     # we can see that the program is not working as required
#     # to fix this we need to include this conditionl within a loop
#     # to allow Python to treat the code as a block
# while True:
#     choice = input("choose 1 or 2\n 1. Water\n 2. Tea\n")
#     if choice == "1":
#         print("your choice is 1")
    
#     elif choice == "2":
#         print("your choice is 2")
#     else:
#         print("this is an invalid input?!!!")
#         choice = input("choose 1 or 2\n 1. Water\n 2. Tea\n")
        # the code is repeated but another problem rises here 
        # it takes two inputs to get back to the normal behavior of the program
        # to fix this, function will be more efficient
        # check this 
def check_invalid():
    choice = input("choose 1 or 2\n 1. Water\n 2. Tea\n")
    if choice == "1":
        print("your choice is 1")
    elif choice == "2":
        print("your choice is 2")
    else:
        print("this is an invalid input?!!!")
        # instead of reprinting the choice again we can call the function itself
        check_invalid()
# do not forget to call the function at the global scope 
check_invalid()
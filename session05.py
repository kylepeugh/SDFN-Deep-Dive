# 1. Print descriptions of what's happening for the player
print("hello player, this game is about..........")
# 2. Pausing between printing descriptions
    # to add a delay to your message, the time module should be imported
import time
    # to use the delay, sleep method should be used like this
print("this will be printed with no delay....")
time.sleep(5) # the argument is the number of seconds 
print("this will be printed after 5 second delay....")
# 3. Give the player some choices
    # the game should ask the player to choose between two options
    # to do this you have to collect the user input like this
user_choice = input("choose your drink 1. water 2. tea")
# 4. Make sure the player gives a valid input
    # now, to keep the game play easy and consistent, options should be like 1 or 2
    # to check invalid input, you have to use a conditional like this3
if user_choice == 1:
    print("your choice is 1")
elif user_choice == 2:
    print("your choice is 2")
else:
    print("this is an invalid input?!!!")
    # if you test this with an invalid input, you can see the game will be terminated
    # to avoid this, we have to ask the player again
    user_choice = input("choose your drink 1. water 2. tea")
    # we can see that the program is not working as required
    # to fix this we need to include this conditionl within a loop
    
# 5. Add functions and refactor your code
# 6. Use randomness in your game
# 7. Create win and lose conditions
# 8. Check if the player wants to play again
# 9. Check your style with pycodestyle
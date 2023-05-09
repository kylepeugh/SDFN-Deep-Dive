# 1. import the modules
import random
import time

# 2. start with the delay function
def delay(period, msg):
    time.sleep(period)
    print(msg)

# 3. Introduce the game to your player
def intro():
    delay(2,"You find yourself in a Jungle")
    delay(2,"To escape, you have to choose your direction") 
    delay(2,"You will have an enemy to fight") 
    delay(2,"You win if you kill the enemy")
    delay(2,"You lose if the enemy killed you")
    delay(2,"At your right there is a cave, at your left there is a creepy house")

# 4. Refactor the check_invalid function to use it correctly
def check_invalid(option1, option2):
    choice = input(f"choose 1 or 2\n 1. {option1}\n 2. {option2}\n")
    if choice == "1":
        return 1
    elif choice == "2":
        return 2
    else:
        print("this is an invalid input?!!!")
        check_invalid(option1, option2)
# 5. refactor the play agian function
def play_again(enemy):
    option = input("Do you like to play again?\n 1. Yes\n 2. No\n")
    if option == "1":
        # you have to start the game again
        play()
    elif option == "2":
        # a goodbye message and terminate the game
        print("Thanks for playing, see you soon!")
    else:
        # restart the function until you get the correct answer
        play_again()
# 6. Refactor the go function
def go(enemy):
    choice = check_invalid("Go Right", "Go Left")
    if  choice == 1:
        print("You find a Gun, now you can protect yourself against enamies")
        option = check_invalid("Fight", "Runaway")
        if option == 1:
            print(f"your gun is so  powerful, {enemy} is dead!")
            print("You win the game")
            play_again(enemy)
        elif option == 2:
            print(f"you ranaway but  the {enemy} found you")
            print("you lose!")
            play_again(enemy)
        else:
            go(enemy)
    elif choice == 2:
        print(f"Oush, there is {enemy}")
        option = check_invalid("Fight", "Runaway")
        if option == 1:
            print(f"your gun is so  powerful, {enemy} is dead!")
            print("You win the game")
            play_again(enemy)
        elif option == 2:
            print(f"you ranaway but  the {enemy} found you")
            print("you lose!")
            play_again(enemy)
        else:
            go(enemy)
    else:
        go(enemy)

# 7. build a main function to run functions in order -
# this function will be used to induce some randomness

def play():
    enamies = ["monster", "dracula", "ghost", "zombie"]
    enemy = random.choice(enamies)
    intro()
    go(enemy)
play()

# places = ["Jungle" ,"desert", "cave"]
# 

# print("you find yourself in a " + random.choice(places))

# enamies = ["monster", "dracula", "ghost", "zombie"]
# print("suddenly a " + random.choice(enamies) + " appeared!")

# print(f"suddenly a {random.choice(enamies)} appeared!")


# do not forget to call the function at the global scope 



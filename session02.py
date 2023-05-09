# 7. Check if the player wants to play again
    # you need to ask the player if he wants
    # to play again at the end of each game round
    # build a function to achieve this
def play_again():
    option = input("Do you like to play again?\n 1. Yes\n 2. No\n")
    if option == "1":
        # you have to start the game again
        print("here, you have to start your game again")
    elif option == "2":
        # a goodbye message and terminate the game
        print("Thanks for playing, see you soon!")
    else:
        # restart the function until you get the correct answer
        play_again()
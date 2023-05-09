# 5. Use randomness in your game
    # to add randomness, the random module should be imported
import random
    # randomness can be anywhere in your game
    # the goal is to give your player a chance to see 
    # a new version of the game if s/he likes to play more rounds
    # to do so, the choice method can be used like this
places = ["Jungle" ,"desert", "cave"]
    # since you have more than one place, you may use a random place like this
print("you find yourself in a " + random.choice(places))
    # enamies can be randomized too
enamies = ["monster", "dracula", "ghost", "zombie"]
print("suddenly a " + random.choice(enamies) + " appeared!")
    # a good practice is to use the template literals like this
print(f"suddenly a {random.choice(enamies)} appeared!")
    # another method to add randomness is to use the randint method
    # the randint method is used to return a random number between two ranges
    # for example
print(random.randint(5, 11))
    # the randint method can be used in the game scenario like this
    # the player will reach a situation where he has to fight an enemy
    # if he choose to fight, you can use the randint method to return
    # a random hit power like this
choice = input("choose 1 or 2\n 1. Fight\n 2. run\n")
if choice == "1":
    print("you hit your enemy using you gun!")
    print(f"your hit power is  {random.randint(0, 100)}")
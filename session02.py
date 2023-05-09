# 6. Create win and lose conditions
# for a player to win, you have many choices 
    # for example, this is a scenario
        # 1. the player choose to go left or to go right
        # 2. if right, he will find a weapon
        # 3. if left, he will find an enemy
        # 4. evantually, the player will choose to fight an enemy or to runaway
        # 5. if fight, after finding a weapon ----->>> he wins
        # 6. if fight, with no weapon ------------->>> he loses
        # 7. if he runaway ------------->>> he loses
def intro():
    print("You find yourself in a Jungle")
    print("At your right there is a cave, at your left there is a creepy house")
def go():
    intro()
    choice = input("choose 1 or 2\n 1. Go Right\n 2. Go Left\n")
    if choice == "1":
        print("You find a Gun, now you can protect yourself against enamies")
        option = input("choose 1 or 2\n 1. Fight\n 2. Runaway\n")
        if option == "1":
            print("your gun is so  powerful, your enemy is dead!")
            print("You win the game")
        elif option == "2":
            print("you ranaway but  the enemy found you")
            print("you lose!")
        else:
            go()
    elif choice == "2":
        print("Oush, there is a monster")
        option = input("choose 1 or 2\n 1. Fight\n 2. Runaway\n")
        if option == "1":
            print("your gun is so  powerful, your enemy is dead!")
            print("You win the game")
        elif option == "2":
            print("you ranaway but  the enemy found you")
            print("you lose!")
        else:
            go()
    else:
        print("This is not correct!")
        go()
go()

    # this is another scenario
        # 1. the player choose to go left or to go right
        # 2. if right, he will find a weapon 
        # 3. if left, he will find an enemy
        # 4. evantually, the player will choose to fight an enemy or to runaway
        # 5. before fight, run a function to generate a random value
        # for the player weapon and the enemy weapon
        # 6. if fight, enemy weapon power < player weapon power ----->>> he wins
        # 7. if fight, enemy weapon power > player weapon power ----->>> he loses
        # 8. if fight, with no weapon ------------->>> he loses
        # 9. if he runaway ------------->>> he loses
def get_random_pwr():
    import random
    return random.randint(50, 100)

def intro_two():
    print("You find yourself in a Jungle")
    print("At your right there is a cave, at your left there is a creepy house")
def go_two():
    intro_two()
    choice = input("choose 1 or 2\n 1. Go Right\n 2. Go Left\n")
    if choice == "1":
        print("You find a Gun, now you can protect yourself against enamies")
        option = input("choose 1 or 2\n 1. Fight\n 2. Runaway\n")
        if option == "1":
            player_weapon = get_random_pwr()
            enemy_weapon = get_random_pwr()
            if player_weapon > enemy_weapon:
                print(f"your gun power is {player_weapon}, your enemy power is {enemy_weapon}")
                print("You win the game")
            elif player_weapon < enemy_weapon:
                print(f"your gun power is {player_weapon}, your enemy power is {enemy_weapon}")
                print("You lose the game")
        elif option == "2":
            print("you ranaway but  the enemy found you")
            print("you lose!")
        else:
            go_two()
    elif choice == "2":
        print("Oush, there is a monster")
        option = input("choose 1 or 2\n 1. Fight\n 2. Runaway\n")
        if option == "1":
            print("your gun is so  powerful, your enemy is dead!")
            print("You win the game")
        elif option == "2":
            print("you ranaway but  the enemy found you")
            print("you lose!")
        else:
            go()
    else:
        print("This is not correct!")
        go_two()
go_two()
import time
import random
items = []
animals = ["dragon", "troll", "gorgon"]
choice = random.choice(animals)


def print_sleep(print_message):
    print(print_message)
    time.sleep(1)


def random_animal():
    animals = ["dragon", "troll", "gorgon"]
    choice = random.choice(animals)


def intro():
    print_sleep("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_sleep("Rumor has it that a dragon is somewhere around here,"
                " and has been terrifying the nearby village.")
    print_sleep("In front of you is a house.")
    print_sleep("To your right is a dark cave.")
    print_sleep("In your hand you hold your trusty"
                "but not very effective) dagger.")


def direction_sel():
    print_sleep("Enter 1 to knock on the door of the house.")
    print_sleep("Enter 2 to peer into the cave.")
    print_sleep("What would you like to do?")
    print_sleep("(Please enter 1 or 2.)")
    while True:
        direction = input()
        if direction == '1':
            enter_house()
        elif direction == '2':
            enter_cave()
        break


def enter_house():
    print_sleep("You approach the door of the house.")
    print_sleep("You are about to knock"
                f" when the door opens and out steps {choice}!")
    print_sleep(f"Eep! This is the {choice}'s house!")
    print_sleep("The dragon attacks you!")
    fight_run_sel()


def enter_cave():
    print_sleep("You peer cautiously"
                " into the cave.")
    print_sleep("It turns out to be only a very small cave.")
    print_sleep("Your eye catches a glint of metal behind a rock.")
    print_sleep("You have found the magical Sword of Ogoroth!")
    print_sleep("You discard your silly old dagger"
                " and take the sword with you.")
    print_sleep("You walk back out to the field.")
    items.append("sword")
    direction_sel()


def fight_run_sel():
    while True:
        decision = input("Would you like to (1) fight or (2) run away?")
        if decision == '1':
            house_fight_mode()
        else:
            decision == '2'
            direction_sel()
        break


def house_fight_mode():
    while True:
        if "sword" in items:
            print_sleep(f"As the {choice} moves to attack,"
                        "you unsheath your new sword.")
            print_sleep("The Sword of Ogoroth shines brightly in your hand"
                        " as you brace yourself for the attack.")
            print_sleep(f"But the {choice} takes one look at your shiny"
                        " new toy and runs away!")
            print_sleep(f"You have rid the town of the {choice}."
                        " You are victorious!")
            play_again()
        else:
            print_sleep("You feel a bit under-prepared for this,"
                        " what with only having a tiny dagger.")
            print_sleep("You do your best...")
            print_sleep(f"but your dagger is no match for the {choice}.")
            print_sleep("You have been defeated!")
            play_again()


def play_again():
    while True:
        again = input("Would you like to play again? (y/n)")
        if again == 'y':
            print_sleep("Excellent! Restarting the game ...")
            intro()
            break
        else:
            again == 'n'
            print_sleep("Thanks for playing! See you next time.")
        break
    exit()


def play_game():
    random_animal()
    intro()
    direction_sel()


play_game()

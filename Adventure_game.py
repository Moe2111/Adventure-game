import time
import random


def print_p(message):

    print(message)
    time.sleep(2)


def intro():
    print_p("You find yourself standing in an open field, "
            "filled with grass and yellow wildflowers.")

    print_p("Rumor has it that a dragon is somewhere around here,"
            " and has been terrifying the nearby village.")
    print_p("In front of you is a house.")
    print_p("To your right is a dark cave")
    print_p("In your hand you hold your trusty"
            "(but not very effective) dagger.")


def house_entrance():
    print_p("You approach the door of the house.")
    print_p("You are about to knock when the door opens "
            "and out steps a dragon!")
    print_p("Eep, This is the dragon's house")
    print_p("The dragon attacks you!")


def house(sword, swords):
    choice = input("Would you like to (1) fight or (2) run away?\n")
    if choice == "1":
        if "Ogoroth" in sword:
            print_p("As the gorgon moves to attack, "
                    "you unsheath your new sword. "
                    f"{swords} "
                    "in your hand as you brace yourself for the attack.")
            print_p("You attacked the dragon and you finally killed him!")
            print_p("You have rid the town of the gorgon. "
                    "You are victorious!")
            play_again(sword, swords)
        else:
            print_p("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
            print_p("You do your best...")
            print_p("but your dagger is no match for the dragon.")
            print_p("You have been defeated!")
            play_again(sword, swords)
    elif choice == "2":
        print_p("You run back into the field. Luckily,"
                " you don't seem to have been followed.")
        play(sword, swords)
    else:
        print_p("Please choose either 1 or 2")
        house(sword, swords)


def cave(sword, swords):
    print_p("You peer cautiously into the cave.")
    if "Ogoroth" in sword:
        print_p("You've been here before, "
                "and gotten all the good stuff. "
                "It's just an empty cave now.")
        print_p("you walk back to the field")
        play(sword, swords)
    else:
        print_p("It turns out to be only a very small cave.")
        print_p("Your eye catches a glint of metal behind a rock.")
        print_p(f"You have found the magical Sword {swords}")
        print_p("You discard your silly old dagger and "
                "take the sword with you")
        print_p("you walk back out to the field")
        sword.append("Ogoroth")
        play(sword, swords)


def play(sword, swords):
    print_p("Enter 1 to knock on the door of the house.")
    print_p("Enter 2 to peer into the cave.")
    print_p("What would you like to do?")

    passage = input("(PLEASE enter 1 or 2)")
    if passage == '1':
        house_entrance()
        house(sword, swords)

    elif passage == "2":
        cave(sword, swords)

    else:
        print_p("Type either 1 or 2")
        play(sword, swords)


def play_again(sword, swords):
    again = input("Would like to play again? (y/n)")
    if again == 'y':
        play_game()
    else:
        print_p("Bye!")


def play_game():
    lis = ["Soul Edge", " Atlantean Sword", "Buster Sword", "Sword of Truth "]
    swords = random.choice(lis)
    sword = []
    intro()
    play(sword, swords)


play_game()

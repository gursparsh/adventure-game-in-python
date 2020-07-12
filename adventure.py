import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro(items, villan):
    print_pause("You arrived to the dreamland")
    print_pause("You are in front of the big door")
    print_pause("But you need to fight with the " + villan + " .")
    print_pause("To enter this world")


def fight_now(items, villan):
    print_pause("You decided to fight")
    print_pause("After a few moments, you found "
                "yourself with the " + villan + " .")
    if "take_help" in items:
        print_pause("You fought with the " + villan + " .")
        print_pause("You Won!")
        play_again()

    else:
        print_pause("You  are alone and you lost")
        play_again()


def take_help(items, villan):
    print_pause("You took help from the villagers")
    print_pause("After a few moments, you find yourself "
                "with the villagers")
    if "take_help" in items:
        print_pause("You already called them")
        print_pause("They are with you")
        intro_two(items, villan)
    else:
        print_pause("Villagers are with you now")
        items.append("take_help")
        intro_two(items, villan)


def run_away(items, villan):
    print_pause("You decided not to enter the DREAMLAND")
    print_pause("After a few moments, you ran ")
    print_pause("You are saved")
    play_again()


def play_again():
    again = input("Would you like to play again?(y/n)").lower()

    if again == "y":
        print_pause("Welcome")
        play_game()
    elif again == "n":
        print("Goodbye!")
        exit()
    else:
        print("Enter valid input(y/n)")
        play_again()


def play_now():
    value == input("What would you like to do now?")
    intro_two(items, villan)


def intro_two(items, villan):
    print_pause("Please enter the choice "
                "of what you would like to do:")
    tools = input("1. Fight\n"
                  "2. Take help\n"
                  "3. Run Away\n")
    if tools == '1':
        fight_now(items, villan)
    elif tools == '2':
        take_help(items, villan)
    elif tools == '3':
        run_away(items, villan)
    else:
        print("Please enter valid input(1,2,3)")
        return intro_two(items, villan)


def play_game():
    items = []
    villan = random.choice(["Berberoka", "Bannik", "Sluagh", "Gan Ceanach"])
    intro(items, villan)
    intro_two(items, villan)


play_game()

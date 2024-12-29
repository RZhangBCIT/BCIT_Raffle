from collections import Counter
import random

namelist = ["regina", "cady", "karen", "regina", "gretchen", "karen", "cady", "janis", "damian"]


def show_players():
    if len(namelist) < 1:
        print("There are currently no players in the raffle!")
    else:
        dict_of_names = Counter(namelist)
        print("-------------------------------- LIST OF PARTICIPANTS --------------------------------")
        for key in dict_of_names:
            print(key, dict_of_names[key])


def add_name():
    name_to_add = input("Please enter the name that you wish to add: \n")
    num_entries = input("How many entries will this player be receiving?\n")
    while not num_entries.isdigit():
        num_entries = input("Please enter a number: \n")
    num_to_add = int(num_entries)
    while num_to_add > 0:
        namelist.append(name_to_add)
        num_to_add -= 1
    print("successfully added " + num_entries + " entries for " + name_to_add + "\n")


def get_command():
    return input("\nEnter 1 to input names, 2 to display current participants, 3 to start the raffle,"
                 "or EXIT to exit the raffle. \n")


def remove_name(name):
    for i in range(namelist.count(name)):
        namelist.remove(name)


def run_raffle():
    num_draws = input("How many raffles draws would you like to make?\n")
    while not num_draws.isdigit():
        num_draws = input("Please enter a number\n")
    draws = int(num_draws)
    while draws > 0:
        draw_command = ["YES", "NO"]
        name_selected = random.choice(namelist)
        is_present = input("Is " + name_selected + " present? Please enter yes or no.\n")
        while is_present.upper() not in draw_command:
            is_present = input("That was not a valid response. Please enter yes if they are present,"
                               "or no if they are not.\n")
        if is_present.upper() == "YES":
            print("Congratulations! " + name_selected + " is a winner! Enjoy your prize!\n")
            remove_name(name_selected)
            draws -= 1



def main():
    print("Hello! Raffle-bot online. Welcome to the BCIT BGA's MTG raffle!")
    list_of_valid_commands = ["1", "2", "3", "EXIT"]
    command = get_command()
    while command.upper() != "EXIT":
        while command.upper() not in list_of_valid_commands:
            print("I'm sorry, it seems you have entered an invalid command.\n")
            command = get_command()
        if command == "1":
            add_name()
            command = get_command()
        elif command == "2":
            show_players()
            command = get_command()
        elif command == "3":
            run_raffle()
            command = get_command()
    print("Thank you for participating in the BCIT BGA's MTG raffle. See you next time!")


if __name__ == "__main__":
    main()

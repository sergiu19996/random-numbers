import random
import re
from simple_term_menu import TerminalMenu


def main_menu():
    """
    Display the main menu of the game and handle user selections.
    """
    options = ["Learn the rules", "Play the game", "Exit"]
    terminal_menu = TerminalMenu(options)
    while True:
        menu_entry_index = terminal_menu.show()
        if options[menu_entry_index] == "Learn the rules":
            print_rules()
            go_back()
        elif menu_entry_index == 1:
            print("Let's play!")
            guess(100)
            go_back()
        elif menu_entry_index == 2:
            print("Exiting the game.")
            exit()
        else:
            return


def print_rules():
    """
    Print the rules of the game.
    """
    print("\nRules of the game:")
    print("1. You have to guess a number between 1 and 100.")
    print("2. You will be provided feedback after each guess.")
    print("3. Keep guessing until you get it right!\n")


def go_back():
    """
    Display the option to go back to the main menu.
    """
    options = ["Go back to main menu"]
    go_back_menu = TerminalMenu(options)
    while True:
        menu_entry_index = go_back_menu.show()
        if menu_entry_index == 0:
            main_menu()


def guess(x):
    """
    Allow the user to guess a number between 1 and x.
    """
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        user_input = input(f"Guess a number between 1 and {x}: ")
        if re.match("^[0-9]+$", user_input):
            guess = int(user_input)
            if guess < random_number:
                print("Sorry, wrong number. Too low.")
            elif guess > random_number:
                print("Sorry, guess again. Too high.")
        else:
            print("Please enter a valid number.")
    print("Congratulations! You guessed the correct number!")


def main():
    """
    The main function of the program.
    """
    print("Welcome to the Number Guessing Game!")
    main_menu()


if __name__ == "__main__":
    main()
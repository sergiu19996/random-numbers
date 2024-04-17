import random


def main_menu():
    """
    Display the main menu and handle user selection.
    """
    options = ["1 learn the rules", "2 play the game", "3 exit"]
    while True:
        print("\nMain Menu:")
        for index, option in enumerate(options):
            print(f"{index + 1}. {option}")
        print('before input')
        choice = input("Please choose an option: ")
        print('after input')
        if choice == "1":
            print_rules()
            go_back()
        elif choice == "2":
            print("GAME")
            guess()
            go_back()
        elif choice == "3":
            print("EXIT")
            exit()
        else:
            print("Invalid choice. Please choose again.")


def print_rules():
    """
    Print out the rules of the game.
    """
    print("\nGame Rules:")
    print("1. Guess a number between 1 and 20.")
    print("2. You have unlimited tries to guess the correct number.")
    print("3. Keep guessing until you find the correct number.")
    print("4. Have fun and good luck!")


def go_back():
    """
    Display a back option menu and handle user selection.
    """
    options = ["go back to main menu"]
    while True:
        print("\nBack Menu:")
        for index, option in enumerate(options):
            print(f"{index + 1}. {option}")
            choice_goback = input("Please choose an option: ")
        if choice_goback == "1":
            main_menu()
        else:
            print("Invalid choice. Please choose again.")


def guess():
    """
    Generate a random number between 1 and 20 and let the user guess it.
    """
    random_number = random.randint(1, 20)
    while True:
        user_input = input('Guess a number between 1 and 20: ')
        if not user_input.isdigit():
            print("Please enter a valid number between 1 and 20.")
            continue
        user_guess = int(user_input)
        if user_guess < 1 or user_guess > 20:
            print("Please enter a number between 1 and 20.")
        elif user_guess < random_number:
            print('Sorry, wrong number. Too low')
        elif user_guess > random_number:
            print('Sorry, guess again. Too high.')
        else:
            print('Yay, you guessed it!')
            break


def main():
    """
    Start the game by displaying a welcome message and showing the main menu.
    """
    print("Hey!")
    main_menu()


if __name__ == "__main__":
    main()
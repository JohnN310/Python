import time

def print_pause(message):
    print(message)
    time.sleep(2)

def intro():
    print_pause("Welcome to the Adventure Game!")
    print_pause("You find yourself in a mysterious forest.")
    print_pause("Your goal is to find the hidden treasure.")
    print_pause("Good luck on your adventure!")

def choose_path():
    print_pause("You come across a fork in the path.")
    print_pause("Which path will you choose? (1 or 2)")
    choice = input("1. Take the left path\n2. Take the right path\n")

    if choice == '1':
        print_pause("You follow the left path and encounter a wild tiger.")
        print_pause("You lose the battle. Game Over!")
        play_again()
    elif choice == '2':
        print_pause("You take the right path and find a hidden trap.")
        print_pause("You trigger the trap. Game Over!")
        play_again()
    else:
        print_pause("Sorry, I didn't understand that.")
        choose_path()

def play_again():
    print_pause("Would you like to play again? (yes or no)")
    choice = input().lower()

    if choice == 'yes':
        print_pause("Great! Restarting the game...")
        start_game()
    elif choice == 'no':
        print_pause("Thank you for playing! Goodbye.")
    else:
        print_pause("Sorry, I didn't understand that.")
        play_again()

def start_game():
    intro()
    choose_path()

start_game()

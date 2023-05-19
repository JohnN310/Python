import time

def print_pause(message):
    print(message)
    time.sleep(2)

def intro():
    print_pause("Welcome to the Jungle Adventure Game!")
    print_pause("You find yourself in a dense jungle.")
    print_pause("Your goal is to find the hidden treasure.")
    print_pause("But beware of wild animals and traps!")
    print_pause("Good luck on your adventure!")

def choose_path():
    print_pause("You come across a fork in the path.")
    print_pause("Which path will you choose? (1 or 2)")
    choice = input("1. Take the left path\n2. Take the right path\n")

    if choice == '1':
        print_pause("You follow the left path.")
        encounter_wild_animal()
    elif choice == '2':
        print_pause("You take the right path.")
        find_traps()
    else:
        print_pause("Sorry, I didn't understand that.")
        choose_path()

def encounter_wild_animal():
    print_pause("Oh no! A wild tiger appears!")
    print_pause("You must make a quick decision.")
    print_pause("What will you do? (1 or 2)")
    choice = input("1. Fight the tiger\n2. Run away\n")

    if choice == '1':
        print_pause("You bravely fight the tiger.")
        print_pause("But it's too strong and you lose the battle.")
        game_over()
    elif choice == '2':
        print_pause("You wisely choose to run away.")
        print_pause("You find yourself back at the fork in the path.")
        choose_path()
    else:
        print_pause("Sorry, I didn't understand that.")
        encounter_wild_animal()

def find_traps():
    print_pause("You stumble upon a field filled with traps!")
    print_pause("You need to navigate carefully.")
    print_pause("What will you do? (1 or 2)")
    choice = input("1. Jump over the traps\n2. Try to go around them\n")

    if choice == '1':
        print_pause("You attempt to jump over the traps.")
        print_pause("But you miscalculate and trigger a trap.")
        game_over()
    elif choice == '2':
        print_pause("You decide to go around the traps.")
        print_pause("It takes some time, but you make it through safely.")
        print_pause("You continue on your journey.")
        treasure_room()
    else:
        print_pause("Sorry, I didn't understand that.")
        find_traps()

def treasure_room():
    print_pause("You finally reach the treasure room!")
    print_pause("Congratulations! You've found the hidden treasure!")
    print_pause("You are victorious!")

def game_over():
    print_pause("Game Over!")
    play_again()

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

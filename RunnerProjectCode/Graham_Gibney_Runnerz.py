import runnerFunctions

def displayMenu():
    print()
    print("Main Menu")
    print("=" * 9)
    print("1. Show the results for a race")
    print("2. Add the results for a race")
    print("3. Show all competitors by country")
    print("4. Show the winner of each race")
    print("5. Show all the race times for one competitor")
    print("6. Show all competitors who have won a race")
    print("7. Quit")


def mainMenuChoice():
    main_choice = runnerFunctions.get_choice_1_7("Please enter your choice: ")
    return main_choice


def performMainChoice(main_menu_choice):
    if main_menu_choice == 1:
        print("1")
    elif main_menu_choice == 2:
        print("2")
    elif main_menu_choice == 3:
        print("3")
    elif main_menu_choice == 4:
        print("4")
    elif main_menu_choice == 5:
        print("5")
    elif main_menu_choice == 6:
        print("6")
    else:
        print("Thanks")


def main():
    displayMenu()
    main_menu_choice = mainMenuChoice()
    performMainChoice(main_menu_choice)


if __name__ == '__main__':
    main()
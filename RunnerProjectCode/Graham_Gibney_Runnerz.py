# Name: Graham Gibney
# SID: R00206659
# Group DY
# Runner's Project - Semester 2

# use validation functions when getting a choice
import runnerFunctions

# simple function to display the Main Menu only
def displayMenu():
    # fancy format when everything is confirmed working
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


# get the user's choice from the main menu - with validation from imported function
# making use of the between 1 and 7 choice validation
def mainMenuChoice():
    main_choice = runnerFunctions.get_choice_1_7("Please enter your choice: ")
    return main_choice


def race_selection_menu():
    print()
    print("Pick a race to review: ")
    print("1: Currabinny")
    print("2: Glengarriff")


def race_menu_choice():
    race_choice = runnerFunctions.get_choice_1_2("Please enter the race results you want to see: ")
    return race_choice


def perform_race_choice(race_choice):
    if race_choice == 1:
        connection = open("currabinny.txt")
        results = connection.read()
        print(results)
    else:
        connection = open("glengarriff.txt")
        results = connection.read()
        print(results)

def act_on_opt1():
    race_selection_menu()
    race_choice = race_menu_choice()
    perform_race_choice(race_choice)

# pass the user's choice into this function to perform the relative menu action
# current variation is to debug/make sure the choice does something ****
def performMainChoice(main_menu_choice):
    if main_menu_choice == 1:
        act_on_opt1()
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


# the main function to hold all separate functions
def main():
    # display the Main Menu to the User
    displayMenu()
    # get the user's choice
    main_menu_choice = mainMenuChoice()
    # act on that main menu choice
    performMainChoice(main_menu_choice)



# main function
if __name__ == '__main__':
    main()
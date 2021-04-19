# Name: Graham Gibney
# SID: R00206659
# Group DY
# Runner's Project - Semester 2

# use validation functions when getting a choice
import runnerFunctions


# simple function to display the Main Menu only
def display_menu():
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
def main_menu_choice():
    main_choice = runnerFunctions.get_choice_1_7("Please enter your choice: ")
    return main_choice


# pass the user's choice into this function to perform the relative menu action
# current variation is to debug/make sure the choice does something ****
def perform_main_choice(main_choice):
    if main_choice == 1:
        choose_race()
    elif main_choice == 2:
        print("2")
    elif main_choice == 3:
        print("3")
    elif main_choice == 4:
        print("4")
    elif main_choice == 5:
        print("5")
    elif main_choice == 6:
        print("6")
    else:
        print("Thanks")


def read_venues(race_file):
    connection = open(race_file)
    lines = connection.readlines()
    connection.close()
    return lines


def make_the_list(lines):
    race_list = []
    for line in lines:
        race_list.append(line.rstrip())
    return race_list


def split_to_two_lists(runner_file):
    connection = open(runner_file)
    names = []
    ids = []
    while True:
        line = connection.readline()
        if line == '':
            break
        line_list = line.rsplit(',')
        names.append(line_list[0])
        ids.append(line_list[1].rstrip())
    return names, ids


def choose_race():
    print("Choose: ")
    print('1. Currabinny')
    print('2. Glengarriff')
    choice = int(input("Please enter a choice: "))
    return choice


def open_file(choice, race_list):
    title = ''
    print("TEST 1:", race_list)
    for i in range(len(race_list)):
        if i == choice:
            title = (race_list[i]).lower()
    print("TEST 2:", title)
    file = open("{}.txt".format(title))
    print("TEST 3:", file.read())


# the main function to hold all separate functions
def main():
    # Turn Races.txt into a string list
    race_file = 'Races.txt'
    lines = read_venues(race_file)
    race_list = make_the_list(lines)
    # Turn Runners.txt into 2 lists
    runner_file = 'Runners.txt'
    runner_names, runner_ids = split_to_two_lists(runner_file)
    # display the Main Menu to the User
    display_menu()
    # # get the user's choice
    menu_choice = main_menu_choice()
    # # act on that main menu choice
    perform_main_choice(menu_choice)
    which_race = choose_race()
    open_file(which_race, race_list)


# main function
if __name__ == '__main__':
    main()
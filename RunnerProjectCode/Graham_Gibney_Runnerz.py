# Name: Graham Gibney
# SID: R00206659
# Group DY
# Runner's Project - Semester 2

# use validation functions when getting a choice
import runnerFunctions


# universal:: decoration
def print_banner():
    print('=' * 20)


# main:: simple function to display the Main Menu only
def display_menu():
    # fancy format when everything is confirmed working
    print()
    print("Main Menu")
    print_banner()
    print("1. Show the results for a race")
    print("2. Add the results for a race")
    print("3. Show all competitors by county")
    print("4. Show the winner of each race")
    print("5. Show all the race times for one competitor")
    print("6. Show all competitors who have won a race")
    print("7. Quit")


# main:: get the user's choice from the main menu - with validation from imported function
# making use of the between 1 and 7 choice validation
def main_menu_choice():
    main_choice = runnerFunctions.get_choice_1_7("Please enter your choice: ")
    return main_choice


# f2:: get the race venue from teh user
def get_race_venue():
    new_venue = input("Where was the race held: ").capitalize()
    return new_venue


# f2:: get the race times for the new venue
def get_runner_times(runner_ids, new_venue, race_file_data):
    print_banner()
    print("Please enter the runner's time in seconds: ")
    print("*** If a runner did not take part, please enter 0 as their time ***")
    print_banner()
    # a new file with the title of the venue is created
    new_file = open("{}.txt".format(new_venue.lower()), 'w')
    for i in range(len(runner_ids)):
        times = int(input(f"Time for {runner_ids[i]}: "))
        # once times are entered, any time > 0 is added to the file
        if times != 0:
            new_file.write(f"{runner_ids[i]},{times}\n")


# f2:: check to see if the race has been recorded already
def check_for_same_race(new_venue, race_list, runner_ids, race_file_data):
    while True:
        if new_venue in race_list:
            print('A file already exists for this race')
            new_venue = get_race_venue()
        else:
            # f2:: if the race has not been recorded
            # print out the list of runners and get their times
            get_runner_times(runner_ids, new_venue, race_file_data)
            # f2:: if the race has not been recorded
            # f2:: add that venue to the race_list
            race_file_data.write(f'\n{new_venue}')

            # race_list.append(new_venue)
            # print(race_list)
            break


# f3:: sort the runners by county and print out a table
def sort_runners(runner_ids, runner_names):
    cork = ""
    kerry = ""
    cork_initials = 'CK'
    kerry_initials = 'KY'
    for i in range(len(runner_ids)):
        if cork_initials in runner_ids[i]:
            cork = cork + f"{runner_names[i]:15s} ({runner_ids[i]}) \n"
        else:
            kerry = kerry + f"{runner_names[i]:15s} ({runner_ids[i]}) \n"
    print()
    print("The Cork Runners are: ")
    print_banner()
    print(cork)
    print("The Kerry Runners are: ")
    print_banner()
    print("Kerry")
    print(kerry)


# main:: pass the user's choice into this function to perform the relative menu action
# current variation is to debug/make sure the choice does something ****
def perform_main_choice(main_choice, race_list, runner_ids, race_file_data, runner_names):
    # # act on that main menu choice
    if main_choice == 1:
        # f1:: iterate through the race list until the index matching choice-1 is found
        which_race = choose_race(race_list)
        # f1:: open the file that matches the string pulled from race_lsit with a littel lower formatting
        open_file(which_race, race_list)
    elif main_choice == 2:
        # f2:: user inpute race venue
        new_venue = get_race_venue()
        # f2:: user adds time for each runner if race is confirmnd new
        check_for_same_race(new_venue, race_list, runner_ids, race_file_data)
    elif main_choice == 3:
        sort_runners(runner_ids, runner_names)
    elif main_choice == 4:
        print("4")
    elif main_choice == 5:
        print("5")
    elif main_choice == 6:
        print("6")


# main:: open the Races.txt file
# pass the lines through to Make the files into a list function
def read_venues(race_file):
    connection = open(race_file)
    lines = connection.readlines()
    connection.close()
    return lines


# main:: turn the Races.txt file into a list of strings
# these strings will be manipulated to pull the correct race info
def make_the_list(lines):
    race_list = []
    for line in lines:
        race_list.append(line.rstrip())
    return race_list


# f1:: split the Runners file into a  Names list and ID list
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


# f1:: split the selected race text file into runner ids list and a times list
def split_races_two_lists(file):
    ids = []
    times = []
    while True:
        line = file.readline()
        if line == '':
            break
        line_list = line.rsplit(',')
        ids.append(line_list[0])
        times.append(line_list[1].rstrip())
    return ids, times


# f1:: display a list of races from the race_list
# get the user to choose from this list
def choose_race(race_list):
    print()
    print("Choose: ")
    num = 1
    for i in range(len(race_list)):
        print(f"{num}. {race_list[i]}")
        num = num + 1
    choice = runnerFunctions.get_integer_choice(f"Please enter a choice: ")
    return choice


# f1:: open the correct file based on the integer choice from the user
def open_file(choice, race_list):
    # the title of the file will be pulled from the race_list
    # if the string in an index slot matches the string pulled from race_list
    # then open that file
    title = ''
    choice = choice - 1
    for i in range(len(race_list)):
        if i == choice:
            title = (race_list[i]).lower()
    file = open("{}.txt".format(title))
    # with the venue results open, split the two entries to runners and times
    ids, times = split_races_two_lists(file)
    # convert the seconds listed into minutes and seconds
    minutes = []
    seconds = []
    times = [float(y) for y in times]
    for m in range(len(times)):
        minutes.append(int(times[m] // 60))
        seconds.append(float(times[m] % 60))
    # print the results and the winners
    print()
    print(f"Results for {title.capitalize()}")
    print("=" * 25)
    for t in range(len(ids)):
        print(f"{ids[t]} {' ' * 5} {minutes[t]} mins {seconds[t]:.0f} seconds.")
    print()
    winner = min(times)
    for q in range(len(times)):
        if times[q] == winner:
            print(f"{ids[q]} won the race!")


# main:: the main function to hold all separate functions
def main():
    # Turn Races.txt into a string list
    race_file = 'Races.txt'
    # f2:: prepare the Races.txt file to be
    # passed to functions for manipulation
    race_file_data = open('Races.txt', 'a')
    lines = read_venues(race_file)
    race_list = make_the_list(lines)
    # Turn Runners.txt into 2 lists
    runner_file = 'Runners.txt'
    runner_names, runner_ids = split_to_two_lists(runner_file)
    # display the Main Menu to the User
    while True:
        display_menu()
        # # get the user's choice
        menu_choice = main_menu_choice()
        perform_main_choice(menu_choice, race_list, runner_ids, race_file_data, runner_names)
        if menu_choice == 7:
            print('Thank you!')
            break


# main function
if __name__ == '__main__':
    main()
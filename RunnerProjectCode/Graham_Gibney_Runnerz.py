# Name: Graham Gibney
# SID: R00206659
# Group DY
# Runner's Project - Semester 2

# use validation functions when getting a choice
import runnerFunctions


# universal:: decoration
def print_banner():
    print('=' * 25)

# ------------------ all functions called from main function: ---------------------------------------------------


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
        get_winners(race_list)
    elif main_choice == 5:
        print()
        print_banner()
        user_runner = pick_a_racer(runner_names, runner_ids)
        check_presence(user_runner, race_list)
    elif main_choice == 6:
        get_all_winners(race_list, runner_names, runner_ids)


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

# ------------------------ end of functions called from Main  --------------------------------------------------

# ↓-1-↓-1-↓-1-↓-1-↓-1-↓-1- ALL FUNCTIONS CALLED TO MAKE OPTION 1 TO WORK: --------------------------------------


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
        times.append(int(line_list[1].rstrip()))
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
    # resetting num to have correct max limit when a user makes a mistake
    num = num - 1
    choice = runnerFunctions.get_choice_1_count("Please enter a choice: ", num)
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

# ------------------------ end of functions called for function 1  ---------------------------------------------

# ↓-2-↓-2-↓-2-↓-2-↓-2-↓-2- ALL FUNCTIONS CALLED TO MAKE OPTION 2 TO WORK: --------------------------------------


# f2:: get the race venue from teh user
def get_race_venue():
    new_venue = runnerFunctions.get_non_empty_string("Where was the race held: ").capitalize()
    return new_venue


# f2:: get the race times for the new venue
def get_runner_times(runner_ids, new_venue):
    print_banner()
    print("Please enter the runner's time in seconds: ")
    print("*** If a runner did not take part, please enter 0 as their time ***")
    print_banner()
    # a new file with the title of the venue is created
    new_file = open("{}.txt".format(new_venue.lower()), 'w')
    for i in range(len(runner_ids)):
        times = runnerFunctions.get_integer_choice(f"Time for {runner_ids[i]}: ")
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
            get_runner_times(runner_ids, new_venue)
            # f2:: if the race has not been recorded
            # f2:: add that venue to the race_list
            # it is no available immediately to the main menu
            race_list.append(new_venue)
            # update the race file with the name of the new venue
            race_file_data.write(f'\n{new_venue}')
            break


# ------------------------ end of functions called for function 2  ---------------------------------------------

# ↓-3-↓-3-↓-3-↓-3-↓-3-↓-3- ALL FUNCTIONS CALLED TO MAKE OPTION 3 TO WORK: --------------------------------------


# f3:: sort the runners by county and print out a table
def sort_runners(runner_ids, runner_names):
    cork = ""
    kerry = ""
    cork_initials = 'CK'
    # f3:: iterate through the id list
    for i in range(len(runner_ids)):
        # f3:: if index contains 'CK' add it to the Cork string
        if cork_initials in runner_ids[i]:
            cork = cork + f"{runner_names[i]:10s} ({runner_ids[i]}) \n"
        # f3:: otherwise add it to the Kerry string
        else:
            kerry = kerry + f"{runner_names[i]:10s} ({runner_ids[i]}) \n"
    # f3:: table time!
    print()
    print("The Cork Runners are: ")
    print_banner()
    print(cork)
    print("The Kerry Runners are: ")
    print_banner()
    print(kerry)

# ------------------------ end of functions called for function 3  ---------------------------------------------

# ↓-4-↓-4-↓-4-↓-4-↓-4-↓-4- ALL FUNCTIONS CALLED TO MAKE OPTION 4 TO WORK: --------------------------------------


# f4:: Show the winner of each race
def get_winners(race_list):
    # the title of the file will be pulled from the race_list
    # if the string in an index slot matches the string pulled from race_list
    # then open that file
    print()
    print("Venue", ' ' * 9,  "Winner")
    print_banner()
    title = ''
    for i in range(len(race_list)):
        title = (race_list[i]).lower()
        file = open("{}.txt".format(title))
        # with the venue results open, split the two entries to runners and times
        ids, times = split_races_two_lists(file)
        # convert the seconds listed into minutes and seconds
        winner = min(times)
        for q in range(len(times)):
            if times[q] == winner:
                print(f"{title.capitalize():15} {ids[q]:5}")

# ------------------------ end of functions called for function 4  ---------------------------------------------

# ↓-5-↓-5-↓-5-↓-5-↓-5-↓-5- ALL FUNCTIONS CALLED TO MAKE OPTION 5 TO WORK: --------------------------------------


# f5:: Show all the race times for one competitor
def pick_a_racer(runner_names, runner_ids):
    print("Choose a runner to see their times: ")
    # f5:: start a count to display runners and a number to select them
    count = 1
    for i in range(len(runner_names)):
        print(f"{count}. {runner_names[i]:15s} ({runner_ids[i]}) ")
        count = count + 1
    # choice = int(input("Runner: "))
    # resetting count to have proper limits when a choice is called for
    count = count - 1
    print('-' * 40)
    choice = runnerFunctions.get_choice_1_count("Enter your runner here: ", count)
    # f5:: reset choice to 0 to iterate through a string
    choice = choice - 1
    # f5:: setting up a string to receive the runner ID
    wordy_choice = ""
    for w in range(len(runner_ids)):
        if w == choice:
            wordy_choice = runner_ids[w]
    return wordy_choice


# f5:: Show all the race times for one competitor
def check_presence(wordy_choice, race_list):
    # set an empty string to catch the title of a venue
    title = ''
    # set an empty string to start building the results
    results = ''
    # decoration
    print()
    print_banner()
    print(wordy_choice, "Results:")
    print_banner()
    print(f"{'Venue':15s} {'Time':20s}")
    print('-' * 50)
    # iterate through the race list and open a file for each entry in the list
    for i in range(len(race_list)):
        title = (race_list[i]).lower()
        file = open("{}.txt".format(title))
        # split the file into 2 lists, runner id and time
        ids, times = split_races_two_lists(file)
        # iterate through the id list / check if the chosen runner id is in the list
        # if it is in the list, start building the results
        for codes in range(len(ids)):
            if ids[codes] == wordy_choice:
                results = f"{title.capitalize():15s} {times[codes] // 60} mins {times[codes] % 60} seconds"
                # get the time ran by the runner here
                time_ran = times[codes]
                # sort the times list
                times.sort()
                # find where in the list the time comes / make the place out of the number of entries
                for t in range(len(times)):
                    if times[t] == time_ran:
                        index = times.index(time_ran)
                        index = index + 1
                        placed = f" ({index} out of {len(times)})"
                        # combine everything together, results and place and print to screen
                        results =(f"{results:5s}" + f"{placed:>5s}")
                print(results)

# ------------------------ end of functions called for function 5  ---------------------------------------------

# ↓-6-↓-6-↓-6-↓-6-↓-6-↓-6- ALL FUNCTIONS CALLED TO MAKE OPTION 6 TO WORK: --------------------------------------


# f6:: making use of the already split Races.txt and Runners.txt
def get_all_winners(race_list, runner_names, runner_ids):
    # f6:: get an empty list ready to catch the winners
    winner_circle = []
    # f6:: pull out the winning runned ID from every race
    for i in range(len(race_list)):
        # f5:: iterate through the race_list and open every file with a respective title
        # recycling the already inputed split_races_two_lists function
        title = (race_list[i]).lower()
        file = open("{}.txt".format(title))
        ids, times = split_races_two_lists(file)
        winner = min(times)
        for q in range(len(times)):
            if times[q] == winner:
                # f6:: getting something to reference in the ID and Names list
                run_id = ids[q]
                # f6:: iterate through the runner ids list with the winning id
                for r in range(len(runner_ids)):
                    if runner_ids[r] == run_id:
                        # f6:: prep the list to print the format wanted to give the user
                        winner_circle.append(f"{run_id} - {runner_names[r]} ({runner_ids[r]})")
    # f6:: remove any duplicate winners
    no_dupes_list = []
    [no_dupes_list.append(x) for x in winner_circle if x not in no_dupes_list]
    print()
    print("Winners Circle:")
    print_banner()
    for d in range(len(no_dupes_list)):
        print(no_dupes_list[d])

# ------------------------ end of functions called for function 6  ---------------------------------------------


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

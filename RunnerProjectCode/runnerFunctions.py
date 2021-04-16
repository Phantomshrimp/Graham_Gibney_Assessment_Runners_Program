# get a string from the user
# dotted throughout the main program
def get_non_empty_string(prompt):
    while True:
        try:
            choice = input(prompt)
            if len(choice) != 0:
                break
        except:
            print("Value Error: Wrong Datatype")
    return choice


# get a positive integer from the user
def get_integer_choice(prompt):
    while True:
        try:
            choice = int(input(prompt))
            if choice >= 0:
                break
        except:
            print("Value Error: Wrong Datatype")
    return choice


# specifically designed to get a choice from the main menu
# 7 choices
def get_choice_1_7(prompt):
    while True:
        try:
            choice = int(input(prompt))
            if 1 <= choice <= 7:
                break
            else:
                print("Please enter a choice that is between 1 and 7 inclusive!")
        except:
            print("Value Error: Wrong Datatype")
    return choice


# specifically designed to get a choice from the main menu
# 7 choices
def get_choice_1_2(prompt):
    while True:
        try:
            choice = int(input(prompt))
            if 1 <= choice <= 2:
                break
            else:
                print("Please enter a choice that is either 1 and 2")
        except:
            print("Value Error: Wrong Datatype")
    return choice
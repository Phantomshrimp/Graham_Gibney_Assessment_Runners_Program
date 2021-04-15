def get_non_empty_string(prompt):
    while True:
        try:
            choice = input(prompt)
            if len(choice) != 0:
                break
        except:
            print("Value Error: Wrong Datatype")
    return choice


def get_integer_choice(prompt):
    while True:
        try:
            choice = int(input(prompt))
            if choice >= 0:
                break
        except:
            print("Value Error: Wrong Datatype")
    return choice


def get_choice_1_7(prompt):
    while True:
        try:
            choice = int(input(prompt))
            if choice >=1 and choice <= 7:
                break
            else:
                print("Please enter a choice that is between 1 and 7 inclusive!")
        except:
            print("Value Error: Wrong Datatype")
    return choice
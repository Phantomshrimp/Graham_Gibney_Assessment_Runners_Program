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
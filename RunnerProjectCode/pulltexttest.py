
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


def main():
    title =''
    print("Choose: ")
    print('1. Currabinny')
    print('2. Glengariff')
    choice = int(input("Please enter a choice: "))
    print(choice)
    choice = choice - 1
    # Turn Races.txt into a string list
    race_file = 'Races.txt'
    lines = read_venues(race_file)
    race_list = make_the_list(lines)
    print(race_list)
    for i in range(len(race_list)):
        if i == choice:
            title = (race_list[i]).lower()
    print(title)
    file = open("{}.txt".format(title))
    print(file.read())

main()
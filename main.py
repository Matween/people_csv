from date import Date
from person import Person


def create_person():
    """
    Creates a person object

    Returns:
    Person: Person instance

    """

    name = ''
    last_name = ''
    while not name:
        name = input('Enter a name: ')
    while not last_name:
        last_name = input('Enter a last name: ')
    date = create_date()

    print('\n')
    return Person(name, last_name, date)


def create_date():
    """
    Creates a date object

    Returns:
    Date: Date instance

    """

    date = None
    day = 0
    month = 0
    year = 0
    while not date or not Date.valid_date(day, month, year):
        print('Enter a date of birth: ')
        day = int(input('Day: '))
        month = int(input('Month: '))
        year = int(input('Year: '))
        date = Date(day, month, year)

    return date


def read_first_line(filename='people.csv', method='r'):
    """
    Reads the file and returns the first line.

    Parameters:
    arg1 (string): The name of the file to open
    arg2 (string): Method to use when opening file

    Returns:
    string: First line of the file

    """

    with open(filename, method) as current:
        current.seek(0)
        if len(current.read(1)) == 0:
            return ''
        else:
            current.seek(0)
            return current.readline()


def add_person(new_person, filename='people.csv', method='a+'):
    """
    Opens the file and appends new person to it.

    Parameters:
    arg1 (Person): Person object to add to the file
    arg2 (string): The name of the file to open
    arg3 (string): Method to use when opening file

    """

    with open(filename, method) as current:
        if read_first_line().rstrip() != 'name;last_name;birthday;':
            current.write('name;last_name;birthday;\n')
        current.write(new_person.csv() + '\n')


def list_all_people(filename='people.csv', method='r', by='default'):
    """
    Reads the file and adds each line to the list as a Person object.

    Parameters:
    arg1 (string): The name of the file to open
    arg2 (string): Method to use when opening file
    arg2 (string): Sort criteria

    Returns:
    list: List of objects found in the csv file

    """

    people = list()
    with open(filename, method) as current:
        current.seek(0)
        for line in current:
            if line.rstrip() == 'name;last_name;birthday;':
                continue
            props = line.split(';')
            date = props[2].split('.')
            people.append(Person(props[0], props[1], Date(int(date[0]), int(date[1]), int(date[2]))))
    if by == 'first_name':
        people.sort(key=lambda x: x.name)
    elif by == 'last_name':
        people.sort(key=lambda x: x.last_name)
    return people


def print_people(people):
    """
    Iterates through the list and prints each object.

    Parameters:
    arg1 (list): List consisting of Person objects

    """

    print('\n')
    if not people:
        print('There are currently no people. Please add a person first.\n')
        return
    i = 1
    for person in people:
        print(f'{i}. {person}')
        i += 1
    print('\n')


def search(people, value, field):
    """
    Looks for people with certain value for their field.

    If field is name, it checks the name attribute
    in each object and compares it to the provided value.

    Parameters:
    arg1 (list): List of people
    arg2 (string): Value to look for
    arg2 (string): Field to check its value

    Returns:
    filter: Returns filtered results

    """

    if field == 'birthday':
        return filter(lambda x: getattr(x, field).year == int(value), people)

    return filter(lambda x: getattr(x, field) == value, people)


if __name__ == '__main__':
    sort_options = {
        'A': 'first_name',
        'B': 'last_name',
    }

    valid_criteria = {
        '1': 'name',
        '2': 'last_name',
        '3': 'birthday',
    }

    while True:
        print('What would you like to do?')
        print('1. Add Person:')
        print('2. List All People:')
        print('3. Find A Person:')
        print('4. Exit\n')
        action = input('Choose numbers between 1 and 4 for your action: ')
        if action == '1':
            add_person(create_person())
        elif action == '2':
            print('What would you like to sort by?')
            print('A. First Name')
            print('B. Last Name')
            option = input('Choose A or B: ')
            if option.upper() in sort_options.keys():
                print_people(list_all_people(by=sort_options.get(option.upper())))
            else:
                print('Printing non sorted list of people.')
                print_people(list_all_people())
        elif action == '3':
            criteria = input('To search for a person, enter:\n'
                             '1. To search by Name\n'
                             '2. To search by Last Name\n'
                             '3. To search by Year of Birth\n'
                             'Enter criteria: ')
            if criteria in valid_criteria.keys():
                people = list_all_people()
                if len(people) == 0:
                    print('There are no people to search for. Add a person first.\n')
                else:
                    value = input(f'Enter {valid_criteria[criteria]}: ')
                    results = search(people, value, valid_criteria[criteria])
                    print_people(results)
        elif action == '4':
            print('Exiting. Bye!')
            break
        else:
            print('Wrong option. Try again.')

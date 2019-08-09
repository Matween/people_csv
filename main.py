from date import Date
from person import Person


def create_person():
    name = ''
    last_name = ''
    while not name:
        name = input('Enter a name: ')
    while not last_name:
        last_name = input('Enter a last name: ')
    date = create_date()

    return Person(name, last_name, date)


def create_date():
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
    with open(filename, method) as current:
        current.seek(0)
        if len(current.read(1)) == 0:
            return ''
        else:
            current.seek(0)
            return current.readline()


def add_person(new_person, filename='people.csv', method='a+'):
    with open(filename, method) as current:
        if read_first_line().rstrip() != 'name;last_name;birthday;':
            current.write('name;last_name;birthday;\n')
        current.write(new_person.csv() + '\n')


def list_all_people(filename='people.csv', method='r', by='default'):
    people = list()
    with open(filename, method) as current:
        current.seek(0)
        for line in current:
            if line.rstrip() == 'name;last_name;birthday;':
                continue
            props = line.split(';')
            people.append(Person(props[0], props[1], props[2]))
    if by == 'first_name':
        people.sort(key=lambda x: x.name)
    elif by == 'last_name':
        people.sort(key=lambda x: x.last_name)
    return people


def print_people(people):
    i = 1
    for person in people:
        print(f'{i}. {person}')
        i += 1


if __name__ == '__main__':
    sort_options = {
        'A': 'first_name',
        'B': 'last_name',
    }

    while True:
        print('What would you like to do?')
        print('1. Add Person:')
        print('2. List All People:')
        print('3. Find A Person:')
        print('4. Exit')
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
            break
        elif action == '4':
            print('Exiting. Bye!')
            break
        else:
            print('Wrong option. Try again.')




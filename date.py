class Date:
    months = ('January', 'February', 'March', 'April', 'May',
              'June', 'July', 'August', 'September', 'October',
              'November', 'December')

    max_days_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __repr__(self):
        return f'Date({self.day_leading_zero()}, {self.month_leading_zero()}, {self.year})'

    def __str__(self):
        return f'{self.day_leading_zero()}.{self.month_leading_zero()}.{self.year}'

    def day_leading_zero(self):
        if self.day < 10:
            return f'0{self.day}'
        else:
            return f'{self.day}'

    def month_leading_zero(self):
        if self.month < 10:
            return f'0{self.month}'
        else:
            return f'{self.month}'

    @staticmethod
    def valid_date(day, month, year):
        if not Date.is_int(day) or not Date.is_int(month) or not Date.is_int(year):
            print('Enter a valid date, it must have positive integers.')
            return False

        if (day <= 0) or (month <= 0) or (year < 0):
            print('Enter a valid date, it must have positive integers.')
            return False

        if month > 12:
            print('There are 12 months in total. Please enter a number less or equal to 12.')
            return False

        if Date.leap_year(year):
            if month == 2 and day > 29:
                print(f'It is a leap year. {Date.months[month - 1]} can have a maximum of 29 days.')
                return False
            elif day > Date.max_days_of_month[month - 1]:
                print(f'Maximum number of days for {Date.months[month - 1]} is {Date.max_days_of_month[month - 1]}')
                return False
        else:
            if day > Date.max_days_of_month[month - 1]:
                print(f'Maximum number of days for {Date.months[month - 1]} is {Date.max_days_of_month[month - 1]}')
                return False

        return True

    @staticmethod
    def leap_year(year):
        if (year % 4) != 0:
            return False
        elif (year % 100) != 0:
            return True
        elif (year % 400) != 0:
            return False
        else:
            return True

    @staticmethod
    def is_int(number):
        return number == int(number)




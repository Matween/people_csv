class Person:
    def __init__(self, name, last_name, birthday):
        self.name = name
        self.last_name = last_name
        self.birthday = birthday

    def __repr__(self):
        return f'Person({self.name}, {self.last_name}, {self.birthday})'

    def __str__(self):
        return f'{self.name} {self.last_name}, {str(self.birthday)}'

    def csv(self):
        return f'{self.name};{self.last_name};{str(self.birthday)};'

    def get_name(self):
        return self.name

    def get_last_name(self):
        return self.last_name

    def get_birthday(self):
        return self.birthday

    def set_name(self, name):
        self.name = name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_birthday(self, birthday):
        self.birthday = birthday

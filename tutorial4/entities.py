class Person:
    def __init__(self, nric, name):
        self.__nric = nric
        self.__name = name

    def get_nric(self):
        return self.__nric

    def set_nric(self, nric):
        self.__nric = nric

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return '{} with nric {}'.format(self.get_nric(), self.get_name())

class Student(Person):
    def __init__(self, nric, name, gpa):
        super().__init__(nric, name)
        self.__gpa = gpa

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa):
        self.__gpa = gpa
    def __str__(self):
        return '{} with nric {} has {} gpa'.format(self.get_nric(), self.get_name(), self.get_gpa())

class Employee(Person):
    def __init__(self, nric, name, salary):
        super().__init__(nric, name)
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def __str__(self):
        return '{} with nric {} is earning {} per month'.format(self.get_nric(), self.get_name(), self.get_salary())


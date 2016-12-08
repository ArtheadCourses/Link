
class Employee:
    raise_amnt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first.lower() + '.' + last.lower() + '@company.com'
        self.pay = pay

    def get_full_name(self):
        return self.first + " " + self.last

    def __repr__(self):
        return self.__class__.__name__ + "({0}, {1}, {2})".format(self.first, self.last, self.pay)

    def __str__(self):
        return self.get_full_name() + " has a salary of " + str(self.pay)

    def give_raise(self):
        self.pay *= self.raise_amnt


class Developer(Employee):
    raise_amnt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def __str__(self):
        return super().__str__() + " and loves " + self.prog_lang


class Manager(Employee):
    raise_amnt = 1.02


def main():
    emp1 = Employee("John", "Jones", 50000)
    emp2 = Developer("Sue", "Smith", 60000, "Python")
    emp3 = Employee("Jack", "Nelson", 45000)
    emp4 = Manager("Anna", "Miller", 55000)

    print(emp2)

    print(emp4)
    emp4.give_raise()
    print(repr(emp2))
    print(type(emp4))



if __name__ == '__main__':
    main()
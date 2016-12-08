
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first.lower() + '.' + last.lower() + '@company.com'
        self.pay = pay

    def get_full_name(self):
        return self.first + " " + self.last

    def __repr__(self):
        return "Employee({0}, {1}, {2})".format(self.first, self.last, self.pay)

    def __str__(self):
        return self.get_full_name() + " has a salary of " + str(self.pay)

    def __add__(self, other):
        return Employee(self.first, other.last, self.pay+other.pay)



def main():
    emp1 = Employee("John", "Jones", 50000)
    emp2 = Employee("Sue", "Smith", 60000)
    emp3 = Employee("Jack", "Nelson", 45000)
    emp4 = Employee("Anna", "Miller", 55000)

    emp5 = emp1 + emp2 + emp3 + emp4
    print(emp5)

if __name__ == '__main__':
    main()
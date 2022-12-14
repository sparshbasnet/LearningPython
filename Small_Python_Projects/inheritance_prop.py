class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last 
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}' .format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
   
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp (self):
        for emp in self.employees:
            print ('-->', emp.fullname())


developer_1 = Developer('Sarthak', 'Aryal', 20000, 'Python')
developer_2 = Developer('Earling', 'Haland', 10000, 'PHP')
developer_3 = Developer('Gigi', 'Hadid', 60000, 'Java')

manager_1 = Manager('Sneha', 'Basnet', 200000, [developer_1, developer_2])

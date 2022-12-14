
class Employee:

    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


    #class methods is used this way
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    #staticmethods is used this way
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

import datetime
my_date = datetime.date(2022, 6, 19)

print(Employee.is_workday(my_date))
         
emp_1= Employee('Sarthak', 'Aryal', 50000)
emp_2= Employee('Deshna', 'Thapa', 80000)

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Rezis-Magar-100000"
emp_str_3 = "Hero-Hiralal-30000"

new_emp_1 =  Employee.from_string(emp_str_1)

Employee.set_raise_amount(1.05)

# print (new_emp_1.email) 

# print(emp_1.email)
# print(emp_2.email)

# print(emp_1.fullname())
# print(emp_2.fullname())
print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print (Employee.num_of_employees)



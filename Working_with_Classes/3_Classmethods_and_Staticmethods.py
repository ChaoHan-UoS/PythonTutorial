
class Employee:

    num_of_emps = 0  # class variables
    raise_amt = 1.04

    # Constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    # Regular Method of the class
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):  # run class method from its class instead of instances
        cls.raise_amt = amount  # class variable

    # Alternative Constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)  # return a new instance created by Employee(first, last, pay)

    # Normal function, don't operate on the instance or class
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# Employee.set_raise_amt(1.05) # Equivalent to Employee.raise_amt = 1.05
# # emp_1.set_raise_amt(1.05) # Can run class methods from instances, but it doesn't make sense and isn't recommended
# print(Employee.raise_amt)  # 1.05
# print(emp_1.raise_amt)  # 1.05
# print(emp_2.raise_amt)  # 1.05


# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'
#
# new_emp_1 = Employee.from_string(emp_str_1)
#
# print(new_emp_1.email, new_emp_1.pay)


import datetime
my_date = datetime.date(2022, 8, 8)
print(my_date, Employee.is_workday(my_date))


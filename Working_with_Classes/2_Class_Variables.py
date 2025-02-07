# Class variables are shared among all instances of a class.
# Instance variables are set for each instance of the class that we create.

class Employee:
    num_of_emps = 0  # Class variables
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first  # instance variables
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1  # Class variable

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


print(Employee.num_of_emps)
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
print(Employee.num_of_emps, '\n')  # because we instantiated the class Employee twice

print(Employee.raise_amount)  # 1.04
# when we try to access an attribute on an instance, it will first check if the instance contains that attribute,
# and if it doesn't, then the class that it inherits from.
print(emp_1.raise_amount)  # 1.04
print(emp_2.raise_amount)  # 1.04

print(Employee.__dict__)  # the namespace of the class Employee
print(emp_1.__dict__, '\n')  # the namespace of the instance emp_1 does not have the attribute raise_amount, but the class Employee does

emp_1.raise_amount = 1.05  # This actually created the raise_amount attribute within emp_1
print(emp_1.__dict__)
print(Employee.raise_amount)  # 1.04
print(emp_1.raise_amount)  # 1.05
print(emp_2.raise_amount)  # 1.04

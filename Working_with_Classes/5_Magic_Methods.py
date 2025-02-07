# The special methods are also called magic or dunder methods, which allow us to emulate built-in types or implement
# operator overloading. https://docs.python.org/3/reference/datamodel.html#special-method-names

print(1 + 2, 'a' + 'b')  # Same as print(int.__add__(1, 2), str.__add__('a', 'b'))
print(len('test'), '\n')  # print('test'.__len__())


class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # Dunder(Double underscores) Methods
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1)
print(repr(emp_1))  # Equivalent to print(emp_1.__repr__())
print(str(emp_1), '\n')  # Equivalent to print(emp_1.__str__())

print(emp_1 + emp_2)
print(len(emp_1))

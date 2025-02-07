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


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Equivalent to Employee.__init__(self, first, last, pay);
        # similarly, super().fullname() is equivalent to Employee.fullname(self),
        # any self. attribute assigned in Employee.fullname(self) will exist in Developer
        self.prog_lang = prog_lang


class Manager(Employee):
    # Employees who manage the developers

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees  # list

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


# print(help(Developer)) # Method resolution order

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')
dev_3 = Developer('Chao', 'Han', 10000, 'Matlab')
dev_4 = Developer('Emma', 'Smith', 90000, 'Matlab')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1, dev_3])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.add_emp(dev_4)
mgr_1.print_emps()
print('\n')

mgr_1.remove_emp(dev_2)
mgr_1.print_emps()
print('\n')

print(isinstance(mgr_1, Manager), issubclass(Manager, Employee))

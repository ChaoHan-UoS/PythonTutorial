# The property decorator allows us to define methods that we can access like attributes. This allows us to
# implement getters, setters, and deleters.

# class Employee:
#
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
# emp_1 = Employee('John', 'Smith')
# emp_1.first = 'Jim'
#
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname())

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    # getter for email
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    # getter for fullname
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # setter for fullname
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # deleter for fullname
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')
emp_1.fullname = "Corey Schafer"  # Using setter allows us to set the attribute fullname

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)  # Using getter to get the attribute fullname

del emp_1.fullname  # Using deleter to delete the attribute fullname
print(emp_1.first)

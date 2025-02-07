# The __call__ dunder method allows any instance of its class to act like a function.

class Pay:
    total_hours = 0  # class variables
    total_pay = 0

    def __init__(self, hourly_wage):
        self.hourly_wage = hourly_wage  # instance variable

    def __call__(self, hours_worked):
        self.total_hours += hours_worked  # instance variables
        self.total_pay += hours_worked * self.hourly_wage
        return hours_worked * self.hourly_wage


pay = Pay(15)  # Instantiation
print('Week 0:', pay.total_hours, pay.total_pay)
pay(8)  # Return a weekly increment of total_pay; same as pay.__call__(8)
print('Week 1:', pay.total_hours, pay.total_pay)
pay(8)
print('Week 2:', pay.total_hours, pay.total_pay, '\n')


class Manager:
    pay = Pay(15)  # the class variable is an object of another class Pay

    def __init__(self, name):
        self.name = name.lower()


mgr_1 = Manager('Michael')
print('Week 0:', mgr_1.name, mgr_1.pay.total_hours, mgr_1.pay.total_pay)
mgr_1.pay(8)  # Assign the class attribute that acts like a function
print('Week 1:', mgr_1.name, mgr_1.pay.total_hours, mgr_1.pay.total_pay)
mgr_1.pay(8)
print('Week 2:', mgr_1.name, mgr_1.pay.total_hours, mgr_1.pay.total_pay)
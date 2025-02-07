# A positional argument means its position matters in a function call. A keyword argument is a function argument with
# a name label. Passing arguments as keyword arguments means order does not matter.


### Example 1
def hello_func(greeting, name='You', name1='Me'):  # required positional argument greeting has to come before keyword argument name
    return '{}, {}, {}'.format(greeting, name, name1)


print(hello_func('Hi', name1='Corey'), '\n')  # Hi, You, Corey
# The keyword arguments can be passed as positional arguments as long as the order is correct.
print(hello_func('Hi', 'Corey', 'Schafer'), '\n')  # Hi, Corey, Schafer
# A positionL argument can be either be passed in the correct order as a positional argument,
# or be explicitly passed as a keyword argument whose order does not matter.
print(hello_func(name='Corey', greeting='Hi'), '\n')  # Hi, Corey, Me


### Example 2
def student_info(*args, **kwargs):
    print(args)  # a tuple of positional arguments
    print(kwargs)  # a dict of keyword argument pairs


# student_info('Math', 'Art', name='John', age=22)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}
student_info(*courses, **info)  # upack positional and keyword values using * and ** respectively
print('\n')


### Example 3
# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(is_leap(2017),days_in_month(2017, 2))
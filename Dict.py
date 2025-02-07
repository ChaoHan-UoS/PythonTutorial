# Dictionaries allow us to work with key-value pairs in Python.

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# # Add and update values of a dict
# student['phone'] = '555-5555'
# student[[1, 2]] = '555-5555'
# student['name'] = 'Jane'
# student.update({'name': 'Jane', 'age': 26})

# # Remove values
# del student['name']
# age = student.pop('age')

print(student)
# print(age)

# print(student['name'])
# print(student.get('name'))
# print(student.get('phone', 'Not Found'))  # The get method returns none by default or a specified default value for keys that don't exist

print(len(student))  # number of keys in the dictionary
print(student.keys())  # A list of keys
print(student.values())  # A list of values
print(student.items())  # A list of key-value pairs

# for key in student:  # Only loop through the keys
#     print(key)

# for key, value in student.items():  # loop through the key-value pairs
#     print(key, value)


# dict1 = dict(
#     obs='obs',
#     action=2)
#
# dict2 = dict(
#     [('a', 1), ('b', 2)],
#     c=3)
#
# print(dict1, '\n', dict2)

# print(__file__)

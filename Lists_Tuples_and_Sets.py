"""
Lists and Tuples allow us to work with sequential data, and Sets allow us to work with unordered unique values.

list [value1, value2]
Tuple (value1, value2)
Set {value1, value2}
Dict {key1: value1, key2: value2}
"""

"""Lists are mutable objects (can be modified)."""
# Empty Lists
empty_list = []
empty_list = list()

courses_1 = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Education', 'Biology']
nums = [1, 5, 2, 4, 3]

# # Slicing
# print(courses_1[-1])  # the last item
# print(courses_1[:2])  # [courses_1[0], ..., courses_1[1]]
# print(courses_1[2:])  # [courses_1[2], ..., courses_1[-1]]

# # Adding values to a list
# courses_1.append('Art')
# courses_1.insert(0, 'Art')
# courses_1.extend(courses_2)
# print(courses_1)

# # Removing values from a list
# courses_1.remove('Math')
# popped = courses_1.pop()  # pop off the last item
# print(popped)
# print(courses_1)

# # Sorting in place
# courses_1.reverse()
# courses_1.sort()  # Sorted alphabetically
# nums.sort()  # Sorted in ascending order
# courses_1.sort(reverse=True)  # Sorted reverse-alphabetically
# nums.sort(reverse=True)  # Sorted in descending order
# print(courses_1)
# print(nums)

# # Sorting out of place
# sorted_courses_1 = sorted(courses_1)  # Sorted alphabetically
# print(sorted_courses_1)

# print(min(nums), max(nums), sum(nums))

# print(courses_1.index('CompSci'))
# print('Math' in courses_1)

# for course in courses_1:
#     print(course)

for index, course in enumerate(courses_1, start=1):
    print(index, course)

# # Turning lists into strings separated by a certain value and the other way around
# course_str = ' - '.join(courses_1)
# new_list = course_str.split(' - ')
# print(course_str)
# print(new_list)

# # access elements in nested lists
# a = [[1,2], [3,4]]
# print(a[1][1])  # 4


"""Tuples are immutable objects."""
# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# # Mutable lists
# list_1 = ['History', 'Math', 'Physics', 'CompSci']
# list_2 = list_1
# print(list_1)
# print(list_2)

# list_1[0] = 'Art'  # Changing the first value of list_1 will also change that of list_2 since they are both the same mutable object
# print(list_1)
# print(list_2)

# # Immutable tuples
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1
# print(tuple_1)
# print(tuple_2)

# # We cannot mutate values of a tuple (append, remove ...) but can loop through and access values.
# tuple_1[0] = 'Art'
# print(tuple_1)
# print(tuple_2)


"""Sets are values that are unordered and have no duplicates."""

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses)  # The order of values change with each execution
print('Math' in cs_courses)  # Sets do the membership test much more efficiently than lists and tuples
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))


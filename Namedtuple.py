# namedtuple returns a new tuple subclass. The first argument you pass to namedtuple becomes the name of the subclass,
# while the list of strings becomes the attributes (data fields). The new subclass is used to create tuple-like objects.

# Named tuple instances do not have per-instance dictionaries, so they are lightweight and require no more memory
# than regular tuples.
# To support pickling, the named tuple class should be assigned to a variable that matches
# typename (Pickling is Python's name for its built in method of serializing an object).
# https://docs.python.org/3/library/collections.html#collections.namedtuple


from collections import namedtuple

# tuple / list
color_tuple = (55, 155, 255)

# dictionary
color_dict = {'red': 55, 'green': 155, 'blue': 255}

# namedtuple
Color = namedtuple('Color', ['red', 'green', 'blue'])  # The returned tuple subclass named Color (RHS) should be assigned to a variable that matches typename (Color, LFS).
# instantiation
color = Color(blue=55, green=155, red=255)  # Equivalently, color = Color(55, 155, 255)
white = Color(255, 255, 255)

print(color, type(color))
print(color.blue)
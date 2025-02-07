# A generator does not hold the entire results in memory rather than yields one result at a time, therefore it
# requires much less memory space than a list, especially when working with large data sets.

def square_numbers(nums):
    for i in nums:
        yield i * i


# my_nums = square_numbers([1,2,3,4,5])
my_nums = (x * x for x in [1, 2, 3, 4, 5])  # Using list comprehension to create the above generator object

# my_nums = [x * x for x in [1, 2, 3, 4, 5]]  # A list [1, 4, 9, 16, 25]

# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))  # Throw an StopIteration exception that means the generator has been exhausted and out of values

print(my_nums)
# print(list(my_nums))  # Converting a generator to a list will lose the advantage over memory efficiency (the whole list needs a large memory space to save).

for num in my_nums:  # The for loop will not show the StopIteration exception
    print(num)

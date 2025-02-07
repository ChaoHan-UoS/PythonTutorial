# An object is iterable means it can be looped over. Specifically, the object needs to return an iterator object from
# its __iter__ method.
#
# An iterator is an object with __next__ method defined that accesses elements in the container one at a time.

nums = [1, 2, 3]

print(dir(nums))

i_nums = iter(nums)
# i_nums = nums.__iter__() # Equivalent to the above statement

print(i_nums)
print(dir(i_nums))

print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
# print(next(i_nums))


for num in nums:
    print(num)

# What the 'for' loop implements in the background is as follows
while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break


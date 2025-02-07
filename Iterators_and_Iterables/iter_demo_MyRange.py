# Create a class behaving like the built-in range function. The class is iterable in the sense it can be used in a
# for loop, but it's also an iterator as it has the __next__ method.
class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


# Using a generator to create an easy-to-read iterator. A generator is an iterator as well with __iter__ and __next__
# implicitly created.
def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


# nums = MyRange(1, 10)  # Using a class
nums = my_range(1, 10)  # Using a generator

print(next(nums))
print(next(nums))
print(next(nums))

# for num in nums:
#     print(num)

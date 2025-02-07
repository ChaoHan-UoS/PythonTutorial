import mem_profile
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print('Memory (Before): {}Mb'.format(mem_profile.memory_usage_resource()))


def people_list(num_people):  # Make a list of dictionaries
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


def people_generator(num_people):  # A generator
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person


# t1 = time.process_time()
# people = people_list(1000000)  # A list of 1M dictionaries
# t2 = time.process_time()

t1 = time.process_time()
people = people_generator(1000000)  # Generator has much less execution time and memory requirement than list,
# especially when working with large data sets; this line can be implemented using list comprehension too
t2 = time.process_time()

# t1 = time.clock()
# people = list(people_generator(1000000))  # When casting the generator to a list, it loses its performance advantage
# t2 = time.clock()

print('Memory (After) : {}Mb'.format(mem_profile.memory_usage_resource()))
print('Took {} Seconds'.format(t2 - t1))

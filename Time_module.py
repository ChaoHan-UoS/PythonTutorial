# https://docs.python.org/3/library/time.html#time.time
# https://www.geeksforgeeks.org/python-time-time-method/
# https://www.tutorialspoint.com/python/time_time.htm#:~:text=Pythom%20time%20method%20time(),better%20precision%20than%201%20second.

"""
time.gmtime([secs]) converts a time expressed in seconds since the epoch to a struct_time in UTC in which the dst
flag is always zero. If secs is not provided or None, the current time as returned by time() is used.
"""

# importing time module
import time

# Get the epoch
obj_epo = time.gmtime(0)  # return an object with a named tuple interface of the time.struct_time class
print(obj_epo, obj_epo.tm_year)  # values of the named tuple can be accessed by index and by attribute name
epoch = time.asctime(obj_epo)
print("epoch is:", epoch)
print('\n')

# Get the current time in seconds since the epoch
time_sec = time.time()
print("Time in seconds since the epoch:", time_sec)

# Current time can be converted into ASCII time
obj = time.gmtime(time_sec)
time_asc = time.asctime(obj)
print("ASCII time:", time_asc)
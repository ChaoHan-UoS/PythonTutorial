# Context Managers are great for when we need to setup or teardown some resources during use. So these can be used
# for: open and closing files, opening and closing database connections, acquiring and releasing locks, and much
# more.

from contextlib import contextmanager


### Using class to build a text manager
class Open_File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


with Open_File('sample.txt', 'w') as f:
    f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

print(f.closed)


### Using function with decorator to build a text manager
@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()


with open_file('sample.txt', 'w') as f:
    f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

print(f.closed)


### Using the Python built-in 'open' context manager
with open('sample.txt', 'w') as f:
    f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

### Equivalent to
# f = open('sample.txt', 'w')
# f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
# f.close()

print(f.closed)

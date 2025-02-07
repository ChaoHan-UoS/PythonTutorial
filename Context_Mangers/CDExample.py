import os
from contextlib import contextmanager

# Without context managers
cwd = os.getcwd()
os.chdir('Sample-Dir-One')
print(os.listdir())
os.chdir(cwd)

cwd = os.getcwd()
os.chdir('Sample-Dir-Two')
print(os.listdir())
os.chdir(cwd)

# Using context managers
@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir('Sample-Dir-One'):
    print(os.listdir())

print(os.getcwd())

with change_dir('Sample-Dir-Two'):
    print(os.listdir())
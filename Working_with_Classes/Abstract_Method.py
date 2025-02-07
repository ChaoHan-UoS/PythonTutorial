# Python by default doesn't support abstract class and abstract method, so there is a package called abc (abstract
# base class) by which we can make a class or method abstract.
#
# Abstract method is a method which only has declaration and doesn't have definition.
#
# A class is called abstract class only if it has at least one abstract method. when you inherit an abstract class as
# a parent to the child class, the child class should define all the abstract method present in the parent class. if
# it is not done, then the child class also becomes an abstract class automatically and python can't instantiate an
# abstract class.

from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    pass

# # Instead, if we define all the abstract method present in the parent class as below, then no error is reported.
# class Laptop(Computer):
#     def process(self):
#         print('Running')

com = Laptop()
# com.process()

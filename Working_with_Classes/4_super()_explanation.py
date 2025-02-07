# Example of diamond/multiple inheritance by super()
# https://www.youtube.com/watch?v=zS0HyfN7Pm4&t=656s


class Grand:
    def __init__(self):
        print('Grand')


class Father(Grand):
    def __init__(self):
        print('Father')
        super().__init__()


class Mother(Grand):
    def __init__(self):
        print('Mother')
        super().__init__()


class Mother2(Grand):
    def __init__(self):
        print('Mother2')
        super().__init__()


class Child(Father, Mother, Mother2):
    def __init__(self):
        print('Child')
        super().__init__()


class GrandChild(Child, Mother2):
    def __init__(self):
        print('GrandChild')
        super().__init__()
        print('\n')
        # run __init__() of the next class in the MRO, i.e., Mother2
        # Equivalent to Mother2.__init__(self)
        super(Mother, self).__init__()


grand_child = GrandChild()
print(help(GrandChild))
print(GrandChild.__mro__)

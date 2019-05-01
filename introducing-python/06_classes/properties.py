class Duck():
    def __init__(self, input_name):
        self.__name = input_name
    def get_name(self):
        print('inside the getter')
        return self.__name
    def set_name(self, input_name):
        print('inside the setter')
        self.__name = input_name
    name = property(get_name, set_name)

class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")
    @staticmethod
    def message():
        print("This message is class-y.")

fowl = Duck('Howard')
print('%s' % fowl.name)
fowl.name = 'Daffy'
print('%s' % fowl.name)

A.kids()
easy_a = A()
hard_a = A()
A.kids()
easy_a.kids()

A.message()
hard_a.message()

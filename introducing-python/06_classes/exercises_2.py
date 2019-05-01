# 6.8
class Element():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

    def __str__(self):
        return ('%s (%s, %s)' %
                        (self.name, self.symbol, self.number))


el = Element('Carbon', 'C', 10)
print(el.name, el.symbol, el.number)
print(el)


# 6.9
class Bear():
    def eats(self):
        return 'berries'
    
class Rabbit():
    def eats(self):
        return 'clover'
    
class Octothorpe():
    def eats(self):
        return 'campers'

b = Bear()
r = Rabbit()
o = Octothorpe()

print('%s eats %s' % (type(b), b.eats()))
print('%s eats %s' % (type(r), r.eats()))
print('%s eats %s' % (type(o), o.eats()))

# 6.10

class Laser():
    def does(self):
        return 'disintegrate'

class Claw():
    def does(self):
        return 'crush'

class SmartPhone():
    def does(self):
        return 'ring'

class Robot():
    def __init__(self):
        self.weapon_1 = Laser()
        self.weapon_2 = Claw()
        self.comm = SmartPhone()

    def does(self):
        '''
        print("Weapons:", type(self.weapon_1), self.weapon_1.does(),
              type(self.weapon_2), self.weapon_2.does(),
              "Communication", type(self.comm), self.comm.does())
        '''
        return '''I have many attachments:
My laser, to %s.
My claw, to %s.
My smartphone, to %s.''' % (
    self.weapon_1.does(),
    self.weapon_2.does(),
    self.comm.does() )
    
r = Robot()
print( r.does() )





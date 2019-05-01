# 6.1
class Thing():
	pass


print(Thing)

example = Thing()
print(example)


# 6.2
class Thing2():
	letters = 'abc'

print(Thing2.letters) # abc

t = Thing2()
t.letters='xxx' # this seems to override the class attribute

t1 = Thing2()

print(t.letters, t1.letters) # xxx abc

Thing2.letters = 'yyy'

print(t.letters, t1.letters) # xxx yyy

print(id(Thing2.letters), id(t.letters), id(t1.letters))

# 6.3
class Thing3():
	def __init__(self):
		self.letters = 'xyz'

try:
	print(Thing3.letters)
except Exception as err:
	print(repr(err))
	

example3 = Thing3()
print('example3.letter =', example3.letters)

# 6.4
class Element():
        def __init__(self, name, symbol, number):
                self.name = name
                self.symbol = symbol
                self.number = number
                
        # 6.6
        def dump(self):
                print(self.name, self.symbol, self.number)

        # 6.7
        def __str__(self):
                return ('%s (%s, %s)' %
                        (self.name, self.symbol, self.number))

el = Element('Hydrogen', 'H', 1)
print(el.name, el.symbol, el.number)

# 6.5
d = { 'name': 'Hydrogen', 'symbol': 'H', 'number': 1 }
hydrogen = Element(**d)
print(hydrogen.name, hydrogen.symbol, hydrogen.number)

# 6.6
hydrogen.dump()

# 6.7
print(hydrogen)

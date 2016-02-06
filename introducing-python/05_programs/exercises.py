from zoo import hours as info
from collections import OrderedDict
from collections import defaultdict

info()

plain = { 'a' : 1, 'b' : 2, 'c' : 3 }
print(plain)

# this will be ordered
fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(fancy)

# this will have a random order, like printing a normal dict
fancy2 = OrderedDict(plain)
print(fancy2)


dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists['a'])


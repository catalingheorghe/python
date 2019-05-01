import re
import string

source = 'Young Frankenstein'

m = re.match('You', source)
if m:
    print(type(m))
    print(m.group())
else:
    print('no match')

m = re.match('Frank', source)
if m:
    print(m.group())
else:
    print('no match')

m = re.match('.*Frank', source)
if m:
    print(m.group())
else:
    print('no match')

m = re.search('Frank', source)
if m:
    print(m.group())
else:
    print('no match')

m = re.findall('n', source)
print(type(m), m)
    
m = re.findall('n.', source)
print(type(m), m)

m = re.findall('n.?', source)
print(type(m), m)

m = re.split('n', source)
print(type(m), m)

m = re.sub('n', '??', source)
print(type(m), m)

printable = string.printable
print(printable[0:(len(printable)//2)])
print(printable[len(printable)//2+1:len(printable)])
m = re.findall('\s', printable) #spaces
print(type(m), m)


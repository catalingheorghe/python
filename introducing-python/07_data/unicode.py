def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value = "%s", name = "%s", value2 = "%s"' %
          (value, name, value2))

unicode_test('A')
unicode_test('#')
unicode_test('\u00a2')
unicode_test('\u20ac')
unicode_test('\u2603') # your font might not have a character to display this

snowman = '\u2603'
print(len(snowman))
ds = snowman.encode('utf-8')
print(repr(ds), len(ds))
print(type(ds), type(snowman))

print('ascii encoding for web pages:',
      snowman.encode('ascii', 'xmlcharrefreplace'))


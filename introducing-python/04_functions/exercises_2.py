# 4.8
def good():
    return ['Harry', 'Ron', 'Hermione']

print(good())

# 4.9
def get_odds():
    for num in range(1, 10, 2):
        yield num

count = 0
for x in get_odds():
    count += 1
    if count == 3:
        print(x)
        break
    
# the solution from the answers section
# uses enumerate(iterable, start) which return a tuple (count, element)
for x in enumerate(get_odds(), 1):
    print(x)
    count, num = x
    if count == 3:
        print(num)
        break

# 4.10
def test(func):
    def new_function(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_function

def foo():
    print('foo')

test_foo = test(foo)
test_foo()

@test
def foo2():
    print('foo2')

foo2()





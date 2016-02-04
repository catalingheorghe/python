# 4.1
guess_me = 7
if guess_me < 7:
    print('too low')
elif guess_me > 7:
    print('too high')
else:
    print('just right')

# 4.2
start = 1
while True:
    if start < guess_me:
        print('too low')
    if start == guess_me:
        print('found it')
        break
    if start > guess_me:
        print('oops')
        break
    start += 1

# 4.3
l = [3, 2, 1, 0]
for x in l:
    print(x)

# 4.4
even_no = [ num for num in range(10) if num % 2 == 0 ]
print(even_no)

# 4.5
squares = { key : key ** 2 for key in range(10) }
print(squares)

# 4.6
odd = { num for num in range(10) if num % 2 == 1 }
print(type(odd), odd)

# 4.7
for x in ('Got %s' % num for num in range(10)):
    print(x)




    

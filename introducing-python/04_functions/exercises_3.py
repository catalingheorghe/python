# 4.11
class OopsException(Exception):
    pass

#raise OopsException()

try:
    raise OopsException()
except OopsException as exc:
    print('Caught an Oops')

# 4.12
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nuns turns into a monster', 'A haunter yarn shop']

movies = {}
for key, value in zip(titles, plots):
    movies[key] = value

print(movies)

# shorter, sweeter
m = dict(zip(titles, plots))
print(m)


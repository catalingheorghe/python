years_list = [ 1987, 1988, 1989, 1990, 1991, 1992 ]

print("first five years: %s" % years_list)
print("third birthday:", years_list[3])
print("oldest: %s" % years_list[-1])


things = [ "mozzarella", "cinderella", "salmonella" ]
things[1].capitalize()
print(things)

things[1] = things[1].capitalize()
print(things)

things[0] = things[0].upper()
print(things)

del things[2]
print(things)


surprise = [ "Groucho", "Chico", "Harpo" ]
surprise[-1] = ((surprise[-1].lower())[::-1]).capitalize()
print(surprise)


e2f = { "dog" : "chien",
        "cat" : "chat",
        "walrus": "morse" }
print(e2f)

f2e = {}
for e, f in e2f.items():
    f2e[f] = e
print(f2e)

print(f2e["chien"])

eng = set(e2f.keys())
print(eng)


life = {
    "animals": { "cats" : [ "Henri", "Grumpy", "Lucky" ],
                 "octopi" : [],
                 "emus" : [] },
    "plants": {},
    "others": {} }
print(life)
print(life.keys())
print(life["animals"].keys())
print(life["animals"]["cats"])


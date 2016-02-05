def get_desc():
	"""Return random weather"""
	from random import choice
	poss = ['rain', 'snow', 'sun', 'who cares']
	return choice(poss)



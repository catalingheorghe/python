from duck import Quote, QuestionQuote, ExclamationQuote

class What():
	def who(self):
		return "nobody"
	
	def says(self):
		return "nothing"

def who_says(obj):
	print(obj.who(), 'says', obj.says())

hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
hunted_1 = QuestionQuote('Bugs', "What's up doc")
hunted_2 = ExclamationQuote('Daffy', "It's rabbit season")

w = What()

who_says(hunter)
who_says(hunted_1)
who_says(hunted_2)
who_says(w)




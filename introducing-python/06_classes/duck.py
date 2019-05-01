class Quote():
	def __init__(self, person, words):
		self.person = person
		self.words = words
	
	def who(self):
		return self.person

	def says(self):
		return self.words + '.'

class QuestionQuote(Quote):
	def says(self):
		return self.words + '?'

class ExclamationQuote(Quote):
	def says(self):
		return self.words + '!'

class BabblingBrook():
        def who(self):
                return 'Brook'
        def says(self):
                return 'Babble'
        
def who_says(obj):
        print(obj.who(), 'says', obj.says())

hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
hunted_1 = QuestionQuote('Bugs Bunny', "What's up, doc")
hunted_2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
brook = BabblingBrook()

who_says(hunter)
who_says(hunted_1)
who_says(hunted_2)
who_says(brook)


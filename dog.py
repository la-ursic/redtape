from animal import animal

class dog(animal):
	
	def __init__(self,name,colour,age,breed):
		self.name = name
		self.colour = colour
		self.age = age
		self.breed = breed

	def barks(self):
		return "BARF"
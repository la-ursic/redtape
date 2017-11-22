class bird:
	
	def __init__(self,name,colour,age):
		self.name = name
		self.colour = colour
		self.age = age

	def tweets(self):
		return "PIÜ"
	def drinks(self):
		return "GLUP"
	def set_colour(self,new_colour):
		self.colour = new_colour
class Car:
	
	def __init__(self,name,colour,speed,motor):
		self.name = name
		self.colour = colour
		self.speed = speed
		self.wheels = "4"
		self.motor = motor

	def starts(self):
		print("VROUM el " + self.name)
	def breaks(self):
		print("BOOM")
	def get_colour(self):
		print(self.colour)
	def set_colour(self,new_colour):
		self.colour = new_colour


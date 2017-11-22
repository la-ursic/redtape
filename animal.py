class animal:
		
	def __init__(self,name,colour):
		self.name = name
		self.colour = colour

	def drinks(self):
		return "GLUP"
	def set_name(self,new_name):
		self.name = new_name
from Geometrical_figures import Geometrical_figures

class Rectangle(Geometrical_figures):

	def __init__(self,base,height):
		self.base = base
		self.height = height
	
	def area(self):
		rectangle_area = self.base * self.height
		return rectangle_area
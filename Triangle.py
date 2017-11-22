from Geometrical_figures import Geometrical_figures

class Triangle(Geometrical_figures):

	def __init__(self,base,height):
		self.base = base
		self.height = height
	
	def area(self):
		triangle_area = self.base * self.height / 2
		return triangle_area
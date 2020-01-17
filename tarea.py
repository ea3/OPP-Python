
############## Distance between two points. 

class Line:

	def __init__(self, coor1, coor2):

		self.coor1 = coor1
		self.coor2 = coor2


	def distance(self):

		x1,y1 = self.coor1
		x2,y2 = self.coor2

		return ((x2 - x1)**2 + (y2 - y1)**2)**0.5


########### Slope

	def slope(self):

		x1,y1 = self.coor1
		x2,y2 = self.coor2

		return (y2 -y1) / (x2 - x1)


c1 = (3,2)
c2 = (8 , 10)

myline = Line(c1, c2)
print(myline.distance())

print(myline.slope())


########## Cylinder



class Cylinder:

	def __init__(self, height = 1, radius = 1):

		self.height = height
		self.radius = radius

	def volume(self):
		return self.height * 3.1415 * (self.radius)**2

	def surface_area(self):

		top = 3.1415* (self.radius**2)

		return (2*top) + (2*3.1415*self.radius*self.height)

mycylinder = Cylinder(2,3)

print(mycylinder.volume())












class Dog():

	species = 'mammal'

	def __init__(self, breed, name):

		self.breed = breed
		self.name = name
		

	def bark(self, number):
		print("Woof!! My name is {} and my age is {} years old.".format(self.name, number))



my_dog = Dog("Labrador", "Rusky")

print(my_dog.breed, my_dog.name)
my_dog2=Dog(breed='Labrador', name= 'Sam')

print(my_dog2.breed)




my_dog3 = Dog('Lab', 'Frankie')
print(type(my_dog3.species))

print(my_dog3)


my_dog3.bark(130)


class Circle():

	pi = 3.14

	def __init__(self, radius = 1): 

		self.radius = radius 

	def get_circumference(self):
		return self.radius * self.pi * 2

my_circle = Circle(100)

print(my_circle.pi)
print(my_circle.radius)

print(my_circle.get_circumference())




#####Inheritance


class Animal():

	def __init__(self):
		print("Animal Created")

	def who_am_i(self):
		print("I am an animal")

	def eat(self):
	 	print("I am eating")



myanimal = Animal()
myanimal.eat()
myanimal.who_am_i()
#print(myanimal)







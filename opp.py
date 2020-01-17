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

class Dog(Animal):
	def __init__(self):
		Animal.__init__(self)
		print("Dog created")

	def who_am_i(self):
		print("I am an DOG")

	def bark(self):
		print("Bark WOOOOOOOOOOOOOOF")

mydog = Dog()


mydog.eat()

mydog.who_am_i()

mydog.bark()


########### Polymorphism.

class Cat():

	def __init__(self,name):
		self.name = name

	def speak(self):
		return self.name + "Says Miauuu"


class Lion():

	def __init__(self,name):
		self.name = name

	def speak(self):
		return self.name + "Says GUAUUUUU"



niko = Lion("Niko")
felix = Cat("Felix")

print(niko.speak())
print(felix.speak())


for pet in [niko, felix]:
	print((pet))
	print((pet.speak()))


def pet_speak(pet):
	print(pet.speak())

pet_speak(niko)
pet_speak(felix)




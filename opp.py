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

class Animal():

	def __init__(self, name):
		self.name: name

	#def speak(self):
		#raise NotImplementedError("Subclass must implement this abstract method")

#myanimal2 = Animal('Fred')
#myanimal2.speak()

##################### Magic methods// dunder mthods.

mylist = [1,2,3]
print(len(mylist))

class Sample():
	pass

mysample= Sample()

print(mysample)
print(mylist)

class Book():

	def __init__(self,title, author, pages):
		self.title = title
		self.author = author
		self.pages = pages

	def __str__(self):
		return f"{self.title} by {self.author} "

	def __len__(self):
		return self.pages

	def __del__(self):
		print("A book object has been deleted")

b = Book('Python Rocks', 'Emilio', 200)
print(b)

print(str(b))

print(len(b))


del b
































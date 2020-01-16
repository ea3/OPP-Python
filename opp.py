class Dog():

	species = 'mammal'

	def __init__(self, breed, name):

		self.breed = breed
		self.name = name
		


my_dog = Dog("Labrador", "Rusky")

print(my_dog.breed, my_dog.name)
my_dog2=Dog(breed='Labrador', name= 'Sam')

print(my_dog2.breed)

def bark(self):
	print("Woof")


my_dog3 = Dog('Lab', 'Frankie')
print(type(my_dog3.species))

print(my_dog3)
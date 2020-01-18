class Account:

	
	def __init__(self,owner,balance):

		self.owner = owner
		self.balance = balance

	

	def deposit(self, amount_to_deposit):

		self.balance = self.balance + amount



	def withdraw(self, amount_to_withdraw):

		if (amount_to_withdraw > self.balance):

			return "Not enough money to withdraw"

		else:

			self.balance = self.balance - amount_to_withdraw

			return f"Your new balance is: {self.balance}"

	def __str__(self):
		return f"{self.owner} has {self.balance} available"



account_1 = Account("Emilio", 1000000)









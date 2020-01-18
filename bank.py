class Account():

	
	def __init__(self,owner,balance):

		self.owner = owner
		self.balance = balance

	

	def deposit(self, amount_to_deposit):

		self.balance = self.balance + amount_to_deposit

		return f"You deposited {amount_to_deposit}, your new balance is: {self.balance}"



	def withdraw(self, amount_to_withdraw):

		if (amount_to_withdraw > self.balance):

			return f"Not enough money to withdraw. Your balance is: {self.balance}"

		else:

			self.balance = self.balance - amount_to_withdraw

			return f"Amount withdraw was: {amount_to_withdraw}. Your new balance is: {self.balance}"

	def __str__(self):
		return f"{self.owner} has {self.balance} available"



account_1 = Account("Emilio", 1000000)

print(str(account_1))
print(account_1.deposit(500000))
print(account_1.withdraw(2000000))
print(account_1.withdraw(1500000))












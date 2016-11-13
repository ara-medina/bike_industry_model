import random

class Bicycle(object):
	def __init__(self, name, weight, cost):
		self.name = name
		self.weight = weight
		self.cost = cost


class Shop(object):

	def __init__(self, inventory):
		self.inventory = inventory
		self.prices = {}
		self.can_buy = {}
		self.in_stock = {}

	# a function to determine how many bikes are in stock for each model at the store 
	def stock(self, stock_list):
		bikes = []

		for model in self.inventory:
			bikes.append(model.name)

		self.in_stock = {}

		for i in range(len(stock_list)):
			self.in_stock[bikes[i]] = stock_list[i]


	# a function to determine the price the bike will sell for at the store 
	def price(self):
		for model in self.inventory:
			bike_cost = model.cost * 1.2
			self.prices[model.name] = bike_cost

		print(self.prices)

	# a function to create a dictionary of bikes that a customer can afford to buy 
	def afford(self, customer):
		print(customer.name)

		for model, price in self.prices.items():
			if customer.budget > price:
				self.can_buy[model] = price

		print(self.can_buy)

	# a function to determine how many bikes are left in stock after a purchase is made and what the store's profit is
	def postPurchase(self, customer):
		for model in self.inventory:
			if model.name == customer.purchased[0]:
				self.in_stock[model.name] = self.in_stock[model.name] - 1
				print(self.in_stock[model.name])
				store_profit = model.cost * 0.2 
				print(store_profit)


class Customer(object):
	def __init__(self, name, budget):
		self.name = name
		self.budget = budget
		self.purchased = None

	# a function that models a customer buying a bike and then calculates their remaining funds
	def purchase(self, shop):
		self.purchased = random.choice(list(shop.can_buy.items()))
		print(self.purchased)

		remaining_funds = self.budget - self.purchased[1]
		print(remaining_funds)

		


# Bikes 
Model_100 = Bicycle("Model 100", 11, 100)
Model_200 = Bicycle("Model 200", 12, 200)
Model_300 = Bicycle("Model 300", 13, 300)
Model_400 = Bicycle("Model 400", 14, 400)
Model_500 = Bicycle("Model 500", 15, 500)
Model_600 = Bicycle("Model 600", 16, 600)
Model_700 = Bicycle("Model 700", 17, 700)

# Customers 
bob = Customer("Bob", 200)
stuart = Customer("Stuart", 500)
fred = Customer("Fred", 1000)

# Shops
allegro = Shop([Model_100, Model_200, Model_300, Model_400, Model_500, Model_600])

# Examples
allegro.price()
allegro.afford(bob)
allegro.stock([101, 102, 103, 104, 105, 106])
bob.purchase(allegro)
allegro.postPurchase(bob)













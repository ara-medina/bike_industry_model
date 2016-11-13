from bicycles import Bicycle
from bicycles import Shop
from bicycles import Customer

# Bikes 
model_100 = Bicycle("Model 100", 11, 100)
model_200 = Bicycle("Model 200", 12, 200)
model_300 = Bicycle("Model 300", 13, 300)
model_400 = Bicycle("Model 400", 14, 400)
model_500 = Bicycle("Model 500", 15, 500)
model_600 = Bicycle("Model 600", 16, 600)
model_700 = Bicycle("Model 700", 17, 700)

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

allegro.afford(fred)
fred.purchase(allegro)
allegro.postPurchase(fred)
from bicycles import Bicycle
from bicycles import Shop
from bicycles import Customer

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

from matplotlib import pyplot as plt 
import random
# Create empty arrays for each of the variables
price = []
ratio = []
index = 0  
number = 100
while index < number:
	price.append(random.uniform(18.00, 22.99))
	ratio.append(random.uniform(.1000, 2.000))
	index = index + 1
# Populate the scatter plot
plt.scatter(ratio, price)
plt.show()
print len(price)
print len(ratio)

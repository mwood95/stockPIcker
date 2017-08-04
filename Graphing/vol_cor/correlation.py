import sys
from matplotlib import pyplot as plt

sym = ['QTNA', 'AMD', 'CYTR', 'EDIT', 'CVRS', 'GOOGL', 'CSCO', 'AMZN', 'NVDA']
for symbol in sym:
	print symbol
	f = open("data"+symbol+".txt", "r")
	price = []
	ratio = []
	if f.mode != 'r':
		print"An Error has occured. Closing open file"
		f.close()
	else:
		contents = f.readlines()
		index = 0
		while index != len(contents):
			data = contents[index].split(" ")
			data[1] = data[1].rstrip("\n")
			data[0] = float(data[0])
			data[1] = float(data[1])
			price.append(data[0])
			ratio.append(data[1])
			index = index + 1
		print "Price array: ", len(price)
		print "Ratio array: ", len(ratio)
		f.close()
		plt.scatter(ratio, price, label=symbol)
		plt.show()

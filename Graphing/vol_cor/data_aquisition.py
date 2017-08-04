import ystockquote as stock 
import time
print "Stocks being analyzed:"
sym = ['QTNA', 'AMD', 'CYTR', 'GOOGL', 'CSCO', 'AMZN', 'NVDA'] 
print sym
iteration = 1
while True:
	for symbol in sym:
		# Continuously open file update contents and close safely
		f = open("data"+symbol+".txt", "a+")
		price = stock.get_last_trade_price(symbol)
		vol = float(stock.get_volume(symbol))
		ave_vol = float(stock.get_average_daily_volume(symbol))
		ratio = vol/ave_vol
		ratio = str(ratio)	
		f.write(price)
		# Insert Delimiter
		f.write(" ")
		f.write(ratio)
		f.write("\n")
		f.close()
	print iteration, "Process Completed ..."
	iteration = iteration + 1
	time.sleep(47)



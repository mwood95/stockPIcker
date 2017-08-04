"""
Author: 	Michael Wood
Last Edit: 	6/28/2017
Discription:	This program keeps track of a number of stocks in a users watch list and fetches data from yahoo finance to be displayed
		to the user. For the sake of speed, limit the number of stocks in the watchlist to a handful of interest stocks. This 
		program will be later extended to give the user BUY, SELL, or HOLD signals.
		This version of the program is being updated for use with Python Version 3	
"""
import ystockquote
import time
import os
from matplotlib import pyplot as plt 
# Begin Program with a clear screen
os.system('clear')

# Text color formatting functions

def green_text(string, data):
	print "\033[32m" + string, data, "\033[0m"
def red_text(string, data):
	print "\033[31m" + string, data, "\033[0m"
def magenta_text(string, data):
	print "\033[35m" + string, data, "\033[0m"

# List all stocks that the user wishes to keep track of
watchlist = ('QTNA', 'AMD', 'CYTR', '^IXIC')

# ---------------------------------------------------------------------------------------------------------------------------------------------

# For loop to fetch and display stock information
time_index = [1]
while True:
	for symbol in watchlist:

		# Various calculations to limit the time the program must go out and fetch data
		price = float(ystockquote.get_last_trade_price(symbol))
		open_price = float(ystockquote.get_today_open(symbol))
		todays_return = price - open_price
		percent_change = 100 * (todays_return / open_price)

		# Formatting data to be displayed
		percent_change = format(percent_change, '.2f')
		todays_return = format(todays_return, '.2f')
		time = ystockquote.get_last_trade_time(symbol)
		print "Last Trade: " + time 
		print symbol + " - Comany Name:	" + ystockquote.get_company_name(symbol)
		magenta_text("Price:			", ystockquote.get_last_trade_price(symbol))


		if(price > open_price):
			green_text("Percent change:		", str(percent_change) + "%") 
			green_text("Todays Return:		", todays_return)
		else:
			red_text("Percent change:		", str(percent_change) + "%")
			red_text("Todays Return:		", todays_return)


		print "Open:			", open_price 
		print "Volume:			" + ystockquote.get_volume(symbol)
		print "Daily Average Volume:	" + ystockquote.get_average_daily_volume(symbol)
		
		
		# Checks to see if volume data is present to avoid any errors
		if ystockquote.get_average_daily_volume(symbol) != 'N/A':
		
		
			# Ratio of current share volume to average share volume 
			volume_ratio = float(ystockquote.get_volume(symbol)) / float(ystockquote.get_average_daily_volume(symbol))
			
			if(volume_ratio > 1):
			

				volume_ratio = format(volume_ratio, '.2f')			
				green_text("Volume Ratio:		", volume_ratio)
			else:
				volume_ratio = format(volume_ratio, '.2f')				
				red_text("Volume Ratio:		", volume_ratio)

		else:
			print("Volume Ratio:		Data Unavailable")
			

		print "Short Ratio:		" + ystockquote.get_short_ratio(symbol)
		print "52 Week High:		" + ystockquote.get_52_week_high(symbol)
		print "52 Week Low:		" + ystockquote.get_52_week_low(symbol) 
		
# This will become the part of the program that is used to graph stock data. That portion is still under development

#		plt.plot(time_index, price)
#		plt.show()

		print "\n"
		


	time.sleep(60)
	os.system('clear') # System call to clear screen after cycling through stock data


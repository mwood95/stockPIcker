"""
Author: 	Michael Wood
Last Edit: 	6/28/2017
Discription:	This program keeps track of a number of stocks in a users watch list and fetches data from yahoo finance to be displayed
		to the user. For the sake of speed, limit the number of stocks in the watchlist to a handful of interest stocks. This 
		program will be later extended to give the user BUY, SELL, or HOLD signals.
"""
import ystockquote
import time
import os
def green_text(string, data):
	print "\033[32m" + string, data, "\033[0m"
def red_text(string, data):
	print "\033[31m" + string, data, "\033[0m"
def blue_text(string, data):
	print "\033[34m" + string, data, "\033[0m"

# List all stocks that the user wishes to keep track of
watchlist = ('QTNA', 'AMD', 'CYTR', '^IXIC')

# ---------------------------------------------------------------------------------------------------------------------------------------------

# For loop to fetch and display stock information
while True:
	for symbol in watchlist:
		price = float(ystockquote.get_last_trade_price(symbol))
		company_name = ystockquote.get_company_name(symbol)
		percent_change = (ystockquote.get_change_percent(symbol))
		open_price = float(ystockquote.get_today_open(symbol))
		todays_return = (price - open_price)
		vol = ystockquote.get_volume(symbol)
		daily_average_vol = ystockquote.get_average_daily_volume(symbol)
		short_ratio = ystockquote.get_short_ratio(symbol)
		ft_week_high = ystockquote.get_52_week_high(symbol)
		ft_week_low = ystockquote.get_52_week_low(symbol)

		print symbol + " - Comany Name:	" + company_name 
		blue_text("Price:			", price)
		if(price > open_price):
			green_text("Percent change:		", percent_change) 
			green_text("Todays Return:		", todays_return) 		
		else:
			red_text("Percent change:		", percent_change) 
			red_text("Todays Return:		", todays_return) 		
		print "Open:			", open_price 
		print "Volume:			" + vol
		print "Daily Average Volume:	" + daily_average_vol
		# Checks to see if volume data is present to avoid any errors
		if ystockquote.get_average_daily_volume(symbol) != 'N/A':
			# Ratio of current share volume to average share volume 
			volume_ratio = float(ystockquote.get_volume(symbol)) / float(ystockquote.get_average_daily_volume(symbol))
			if(volume_ratio > 1):

				green_text("Volume Ratio:		", volume_ratio)
			else:
				red_text("Volume Ratio:		", volume_ratio)

		else:
			print "Volume Ratio:		Data Unavailable"

		print "Short Ratio:		" + short_ratio 
		print "52 Week High:		" + ft_week_high 
		print "52 Week Low:		" + ft_week_low
		print "\n"	
	time.sleep(5)
	os.system('clear') # System call to clear screen after cycling through stock data

		
		

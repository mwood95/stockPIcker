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

# List all stocks that the user wishes to keep track of
watchlist = ('QTNA', 'AMD', 'CYTR', '^IXIC')

# ---------------------------------------------------------------------------------------------------------------------------------------------

# For loop to fetch and display stock information
while True:
	for symbol in watchlist:
		print symbol + " - Comany Name:	" + ystockquote.get_company_name(symbol)
		print "Price:			" + ystockquote.get_last_trade_price(symbol)
		print "Percent change:		" + ystockquote.get_change_percent(symbol)
		print "Todays Return:		",  (float(ystockquote.get_last_trade_price(symbol)) - float(ystockquote.get_today_open(symbol)))
		print "Open:			" + ystockquote.get_today_open(symbol)
		print "Volume:			" + ystockquote.get_volume(symbol)
		print "Daily Average Volume:	" + ystockquote.get_average_daily_volume(symbol)
		# Checks to see if volume data is present to avoid any errors
		if ystockquote.get_average_daily_volume(symbol) != 'N/A':
			# Ratio of current share volume to average share volume 
			volume_ratio = float(ystockquote.get_volume(symbol)) / float(ystockquote.get_average_daily_volume(symbol))
			print "Volume Ratio:		", volume_ratio
		else:
			print "Volume Ratio:		Data Unavailable"

		print "Short Ratio:		" + ystockquote.get_short_ratio(symbol)
		print "52 Week High:		" + ystockquote.get_52_week_high(symbol)
		print "52 Week Low:		" + ystockquote.get_52_week_low(symbol)
		print "\n"	
	os.system('clear') # System call to clear screen after cycling through stock data
	time.sleep(10)	
		
		

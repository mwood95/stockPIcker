import ystockquote
everything = dir(ystockquote)
watchlist = ('QTNA', 'AMD', 'CYTR', '^IXIC')
while True:
	for symbol in watchlist:
		print symbol + " - Comany Name:	" + ystockquote.get_company_name(symbol)
		print "Volume:			" + ystockquote.get_volume(symbol)
		print "Daily Average Volume:	" + ystockquote.get_average_daily_volume(symbol)
		if ystockquote.get_average_daily_volume(symbol) != 'N/A':
			volume_ratio = float(ystockquote.get_volume(symbol)) / float(ystockquote.get_average_daily_volume(symbol))
		else:
			print "Volume Ratio:		Data Unavailable"
		print "Volume Ratio:		", volume_ratio
		print "Short Ratio:		" + ystockquote.get_short_ratio(symbol)
		print "52 Week High:		" + ystockquote.get_52_week_high(symbol)
		print "52 Week Low:		" + ystockquote.get_52_week_low(symbol)
		print "\n"	
		
		
		

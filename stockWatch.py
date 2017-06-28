import ystockquote
everything = dir(ystockquote)
watchlist = ('QTNA', 'AMD', 'CYTR', 'IXIC')
while True:
	for symbol in watchlist:
		print "Comany Name: " + ystockquote.get_company_name(symbol)
		print "Volume: " + ystockquote.get_volume(symbol)
		print "Daily Average Volume: " + ystockquote.get_average_daily_volume(symbol)
		print "Price Book: " + ystockquote.get_price_book(symbol)
		print "Ticker Trend: " + ystockquote.get_ticker_trend(symbol)
		print "Short Ratio: " + ystockquote.get_short_ratio(symbol)
		print "52 Week High: " + ystockquote.get_52_week_high(symbol)
		print "52 Week Low: " + ystockquote.get_52_week_low(symbol)
		print " "

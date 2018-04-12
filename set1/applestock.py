stock_prices_yesterday = [10, 7, 5, 4, 2, 1]

def get_max_profit(stocks):
	max_profit = stocks[0] - stocks [1]
	buy = stocks[0]
	for i in range (1, len(stocks)):
		potential_profit = stocks[i] - buy
		if potential_profit > max_profit:
			max_profit = potential_profit
	print(max_profit)
get_max_profit(stock_prices_yesterday)

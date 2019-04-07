'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
'''

class Solution:
	def maxProfit(self,prices: [int])->int:
		if len(prices) <=1:
			return 0

		buy_price = prices[0]
		sell_price = prices[0]
		profit =0
		for i in range(1,len(prices)):
			if prices[i]<=sell_price:
				profit += sell_price - buy_price
				buy_price = prices[i]
				sell_price = prices[i]
			else:
				sell_price = prices[i]
				if i == len(prices)-1:
					profit += sell_price - buy_price
		return profit

def main():
	sol = Solution()
	input = [7,1,10,0,10,2,8]
	output = sol.maxProfit(input)
	print(output)

if __name__ == "__main__":
	main()
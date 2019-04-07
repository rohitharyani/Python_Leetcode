'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
'''
class Solution:
	def maxProfit(self,prices: [int])->int:
		profit = 0
		for i in range(len(prices)):
			for j in range(len(prices)):
				temp = prices[j]-prices[i]
				if temp > profit:
					profit = temp


		return profit

def main():
	sol = Solution()
	input = [2,1,2,1,0,1,2]
	output = sol.maxProfit(input)
	print(output)

if __name__ == "__main__":
	main()

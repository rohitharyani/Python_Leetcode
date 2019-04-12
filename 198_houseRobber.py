'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you from 
robbing each of them is that adjacent houses have security system connected and it will 
automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.
'''

class Solution:
	def rob(self,nums:[int])->int:
		curr = prev = 0
		for x in nums:
			curr, prev = max(curr, prev+x), curr
			print(curr, prev)
		return curr



def main():
	sol = Solution()
	input = [1,2,3,1]
	output = sol.rob(input)
	print(output)

if __name__=="__main__":
	main()
'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

class Solution:
	def climbStairs(self, n:int)->int:
		#implement fibonacci sequence
		if n == 1:
			return 1
		elif n == 2:
			return 2
		else:
			return self.climbStairs(n-1)+self.climbStairs(n-2)



def main():
	sol = Solution()
	output = sol.climbStairs(35)
	print(output)

if __name__ == "__main__":
	main()


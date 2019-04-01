'''
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
'''
class Solution:
	def sqrt(self,x:int)->int:
		#return x to the power of 0.5 
		return int(x**0.5)

def main():
	sol = Solution()
	output = sol.sqrt(4)
	print(output)

if __name__=="__main__":
	main()

'''
Count number of primes less than non-negative n
'''

class Solution:
	def primes(self, n:int)->int:
		count =0 
		init = {0:0,1:0,2:0,3:1,4:2,5:2}
		if n in init:
			return init.get(n) 
		else:
			for i in range(2,n):
				if i%2==0 or i%3==0 or i%5==0:	
					pass		
				else:
					count+=1
					
		return count+3


def main():
	sol = Solution()
	input = 10000
	output = sol.primes(input)
	print(output)
	
if __name__ == "__main__":
	main()


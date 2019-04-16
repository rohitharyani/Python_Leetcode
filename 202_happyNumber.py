<<<<<<< HEAD
'''
A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.
'''

class Solution:
	def happy(self,n:int):
		mem = set()
		while n !=1:
			n = sum([int(i)**2 for i in str(n)])
			if n in mem:
				return False
			else:
				mem.add(n)
			print(mem)
		return True

def main():
	sol = Solution()
	input = 19
	output = sol.happy(input)
	print(output)


if __name__=="__main__":
=======
'''
A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.
'''

class Solution:
	def happy(self,n:int):
		mem = set()
		while n !=1:
			n = sum([int(i)**2 for i in str(n)])
			if n in mem:
				return False
			else:
				mem.add(n)
			print(mem)
		return True

def main():
	sol = Solution()
	input = 19
	output = sol.happy(input)
	print(output)


if __name__=="__main__":
>>>>>>> b58a368f7589ead8231635cc47bbf3b440c9b049
	main()
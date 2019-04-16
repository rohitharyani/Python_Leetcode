<<<<<<< HEAD
'''
Given an integer n, return the number of trailing zeroes in n!
'''

class Solution():
	def trailing(self, n:int)->int:
		count = 0
		while n:
			count+= n//5
			n //=5

		return count


def main():
	sol = Solution()
	input = 5
	output = sol.trailing(input)
	print(output)


if __name__=="__main__":
=======
'''
Given an integer n, return the number of trailing zeroes in n!
'''

class Solution():
	def trailing(self, n:int)->int:
		count = 0
		while n:
			count+= n//5
			n //=5

		return count


def main():
	sol = Solution()
	input = 5
	output = sol.trailing(input)
	print(output)


if __name__=="__main__":
>>>>>>> b58a368f7589ead8231635cc47bbf3b440c9b049
	main()
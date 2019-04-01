'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
'''

class Solution:
	def plusOne(self, digits: [int])->[int]:
		#Convert the list in the number represented
		num = sum(digit*10**i for i,digit in enumerate(digits[::-1]))
		#Add 1 to the number
		num+=1
		#Return list of the value of the number
		return list(map(int,str(num)))



def main():
	sol = Solution()
	output = sol.plusOne([1,2,3])
	print(output)


if __name__ == "__main__":
	main()
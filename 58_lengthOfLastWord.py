'''
Given a string s consists of upper/lower-case alphabets and 
empty space characters ' ', return the length of last word in the string.
If the last word does not exist, return 0.
'''
class Solution:
	def lengthOfLastWord(self, s: str)->int:
		#split string in to words list
		#if word list exists return the length of last word
		#else return 0
		words = s.split()
		if words:
			return len(words[-1])
		else:
			return 0


def main():
	sol = Solution()
	output = sol.lengthOfLastWord("Hello World")
	print(output)


if __name__ == "__main__":
	main()
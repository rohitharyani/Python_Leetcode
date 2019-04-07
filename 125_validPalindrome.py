'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
'''

class Solution:
	def isPlindrome(self,s: str)->bool:
		s = s.lower()
		s = s.replace(" ", "")
		s = "".join(e for e in s if e.isalnum())
		print(s)
		if s == s[::-1]:
			return True
		else:
			return False





def main():
	sol = Solution()
	input = "0P"
	output = sol.isPlindrome(input)
	print(output)


if __name__ == "__main__":
	main() 
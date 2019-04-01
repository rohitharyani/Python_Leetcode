# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		#length for traversal  = length(haystack) - length(needle)
		len_traversal = len(haystack) - len(needle) +1
		#length of needle
		len_needle = len(needle)
		#check if needle exists else return 0
		if needle:
			#check if needle is a substring in haystack else return -1
			if needle in haystack:
				#traverse list to check the position of starting element to length(needle) is equal to value of needle
				#Print starting position
				for i in range(len_traversal):
					if haystack[i:i+len_needle] == needle:
						return i

			else:
				return -1

		else:
			return 0


def main():
	sol = Solution()
	output = sol.strStr("hello", "ll")
	print(output)

if __name__ == "__main__":
	main()
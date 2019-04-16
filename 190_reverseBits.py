'''
Reverse bits of a given 32 bits unsigned integer.

'''
class Solution:
	def reverse(self, n:int)->int:
		s = ""
		for i in range(32):
			s=s+str(n>>i &1)

		return int(s,2)




def main():
	sol = Solution()
	input = 43261596
	output = sol.reverse(input)
	print(output)


if __name__ == "__main__":
	main()
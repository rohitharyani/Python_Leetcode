class Solution:
	def titleNumber(self,s:str)->int:
		alpha = {c: index+1 for index,c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}

		result = 0
		for char in s:
			result = result*26+alpha[char]
			
		return result



def main():
	sol = Solution()
	input = "AAA"
	output = sol.titleNumber(input)
	print(output)


if __name__ == "__main__":
	main()
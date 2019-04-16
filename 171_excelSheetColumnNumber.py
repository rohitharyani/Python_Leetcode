<<<<<<< HEAD
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
=======
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
>>>>>>> b58a368f7589ead8231635cc47bbf3b440c9b049
	main()
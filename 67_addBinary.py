'''
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.
'''
class Solution:
	def addBinary(self,a:str, b:str)->str:
		#using the binary function in python 
		output = bin(int(a,2)+int(b,2))
		return output[2:]

def main():
	sol = Solution()
	output = sol.addBinary("11","1")
	print(output)

if __name__ == "__main__":
	main()
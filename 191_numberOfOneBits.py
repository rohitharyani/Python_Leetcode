'''
Given int find number of 1 bits
'''

class Solution:
	def number(self,n:int)->int:
		out= str(bin(n).replace("0b",""))
		print (out)
		count=0
		for i in out:
			if int(i)&1:
				count+=1
		return count


def main():
	sol = Solution()
	input = 699663
	output = sol.number(input)
	print(output)

if __name__=="__main__":
	main()
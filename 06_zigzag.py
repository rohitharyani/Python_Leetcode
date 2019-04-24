'''
he string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows

'''

import unittest

class Solution:
	def zigzag(self,s:str,numRows:int)->str:
		lines = [""]*numRows
		increment = numRows + (numRows-2)

		if numRows == 1:
			return s
        
		try:
			for index in range(len(s))[::increment]:
				for index_down in range(numRows):
					lines[index_down] += s[index + index_down]
				for index_up in range(numRows)[1:-1]:
					lines[numRows-index_up-1] += s[(index+numRows +index_up - 1)]
		except:
			pass
     	
		return "".join(lines)


class Test(unittest.TestCase):
	def test_zigzag(self):
		sol = Solution()
		data = [("PAYPALISHIRING",3,"PAHNAPLSIIGYIR")]
		for [test,numRows,expected] in data:
			actual = sol.zigzag(test,numRows)
		self.assertEqual(actual,expected)


if __name__ == "__main__":
	unittest.main()
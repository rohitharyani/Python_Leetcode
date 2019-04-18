import unittest

class Solution:
	def myAtoi(self,str:str)->int:
		isNumStarted = False
		number = None
		sign =1
		for e in str:
			if e ==" " and not isNumStarted:
				continue
			elif (e == "-" or e == "+") and not isNumStarted:
				isNumStarted = True
				if e == '+':
					sign =1
				else:
					sign = -1
			elif e.isdigit():
				if not number:
					isNumStarted = True
					number = int(e)
				else:
					number = number*10+int(e)
			else:
				break

		if not number:
			number =0
		else:
			number = number * sign
			if number>=pow(2,31):
				number = pow(2,31)-1
			elif number<pow(-2,31):
				number = pow(-2,31)
		return number



class Test(unittest.TestCase):
	data = [("42","42"), ("4193 with words","4193"), 
	("    word 123456","0")]

	def test_myAtoi(self):
		sol =Solution()
		for [test_string,expected] in self.data:
			actual = str(sol.myAtoi(test_string))
			self.assertEqual(actual, expected)



if __name__=="__main__":
	unittest.main() 
import unittest
class Solution:
	def lengthOfLongestSubstring(self, s:str)->int:
		if not s: return 0
		out, count = [],[]
		temp = 0
		for i in s:
			if i not in out:
				out.append(i)
				temp+=1
			else:
				count.append(temp)
				temp =0
				out.clear()
		if not count:
			return temp
		else:
			return max(temp,max(count))




class Test(unittest.TestCase):
	'''Test Case'''
	data = [("pwwkew",'3')]

	def test_lengthOfLongestSubstring(self):
		sol = Solution()
		for [test_string, expected] in self.data:
			actual = str(sol.lengthOfLongestSubstring(test_string))
			self.assertEqual(actual,expected)


if __name__=="__main__":
	unittest.main()
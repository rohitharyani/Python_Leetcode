'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
'''

class Solution:
	def singleNumber(self, nums:[int]) -> int:
		res = nums[0]
		for i in range(1,len(nums)):
			res = res^nums[i]
		return res


def main():
	sol = Solution()
	input = [1,1,2,2,3,4,5,6,6,5,4]
	output = sol.singleNumber(input)
	print(output)


if __name__ == "__main__":
	main()
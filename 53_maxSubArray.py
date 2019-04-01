#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
class Solution:
	def maxSubArray(self, nums: [int])-> int:
		#Store first element as result and compare the rest subarray to find max
		temp = result = nums[0]
		for i in nums[1:]:
			temp+=i
			temp = max(temp, i)
			if temp > result:
				result = temp
		return result


def main():
	sol = Solution()
	output = sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
	print(output)

if __name__ == "__main__":
	main()
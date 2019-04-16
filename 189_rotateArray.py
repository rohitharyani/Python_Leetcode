'''
Given an array, rotate the array to the right by k steps, where k is non-negative.
'''

class Solution:
	def rotateArray(self,nums:[int], k:int)->[int]:
		if len(nums)<k:
			nums = nums[::-1]
			return nums
		else:

			temp = nums[-1:-1-k:-1]
			diff = len(nums)-k
			for i in range(diff):
				nums[-1-i]=nums[diff-1-i]

			nums[:k] = temp[::-1]

			return nums


def main():
	sol = Solution()
	input = [1,2,3,4,5,6,7,8,9]
	k=4
	output = sol.rotateArray(input,k)
	print(output)


if __name__ == "__main__":
	main()
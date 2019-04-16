<<<<<<< HEAD
'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''

import collections

class Solution:
	def majorityElement(self, nums:[int])->int:

		count = collections.Counter(nums)
		return max(count.keys(),key=count.get)


def main():
	sol = Solution()
	input = [1,2,1,2,5,2,1,2,4,2,1,2,6,2,1]
	output = sol.majorityElement(input)
	print(output)


if __name__ == "__main__":
=======
'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''

import collections

class Solution:
	def majorityElement(self, nums:[int])->int:

		count = collections.Counter(nums)
		return max(count.keys(),key=count.get)


def main():
	sol = Solution()
	input = [1,2,1,2,5,2,1,2,4,2,1,2,6,2,1]
	output = sol.majorityElement(input)
	print(output)


if __name__ == "__main__":
>>>>>>> b58a368f7589ead8231635cc47bbf3b440c9b049
	main()
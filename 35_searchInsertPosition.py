#Given a sorted array and a target value, return the index if the target is found. 
#If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array
class Solution:
	def searchInsert(self,nums: [int], target: int) -> int:
		#enumerate list to search for element or find the index to insert the element
		for i, val in enumerate(nums):
			if val>=target:
				return i
		#return end position for element to be inserted
		return i+1


def main():
	sol = Solution()
	output = sol.searchInsert([1,3,5,6],5)
	print(output)

if __name__ == "__main__":
	main()
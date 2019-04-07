'''Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
Input: 5
Output: 
[
[1],
[1,1],
[1,2,1],
[1,3,3,1],
[1,4,6,4,1]
]
'''

class Solution:
	def generate(self, num_row: int) ->[int]:
		triangle = []

		for row_num in range(num_row):
			#the first and last row elements are always 1
			row = [None for _ in  range(row_num+1)]
			row[0], row[-1] = 1, 1

			#Each triangle element is equal to the sum of the elements
			#above-and-to-the-left and above-and-to-the-right
			for j in  range(1, len(row)-1):
				row[j] = triangle[row_num-1][j-1]+ triangle[row_num-1][j]
			triangle.append(row)
		return triangle

def main():
	sol = Solution()
	input = 5
	output = sol.generate(input)
	print(output)


if __name__ == "__main__":
	main()
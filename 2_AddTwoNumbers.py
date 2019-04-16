'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

class ListNode:
	def __init__(self,x):
		self.val = x
		self.next=None

class Solution:
	def addTwoNumbers(self, l1:ListNode, l2:ListNode)-> ListNode:
		if not l1 or not l2:
			return l1 or l2

		result = ListNode(None)
		current = result
		carry = 0

		while l1 and l2:
			sum = l1.val+l2.val+carry
			carry = sum//10
			current.next = ListNode(sum%10)

			current = current.next
			l1 = l1.next
			l2 = l2.next

		residual = l1 or l2

		if carry != 0:
			residual = self.addTwoNumbers(ListNode(carry), residual)

		current.next = residual

		return result.next



def main():
	sol = Solution()
	l1 = ListNode(5)
	l1_1 = ListNode(2)
	l1.next = l1_1

	l2 = ListNode(5)
	l2_1 = ListNode(2)
	l2.next = l2_1

	output = sol.addTwoNumbers(l1,l2)
	
	final_output = []
	while output:
		final_output.append(output.val)
		output = output.next
	print(final_output)


if __name__ == "__main__":
	main()
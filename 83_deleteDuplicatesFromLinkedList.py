class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def deleteDuplicates(self,head:ListNode)->ListNode:
		
		if head is not None:
			curr_pointer = head
			next_pointer = head.next

			while curr_pointer:
				if next_pointer.val == curr_pointer.val:
					curr_pointer.next = next_pointer.next
					del next_pointer
					next_pointer = curr_pointer.next
				else:
					curr_pointer = next_pointer
					next_pointer = next_pointer.next

			return head
		return head


def main():
	node1 = ListNode(1)
	node2 = ListNode(2)
	node3 = ListNode(3)
	node1.next = node2
	node2.next = node3


	sol = Solution()
	output = sol.deleteDuplicates(node1)
	print(output)

if __name__ == "__main__":
	main()


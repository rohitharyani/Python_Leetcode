<<<<<<< HEAD
'''
Write a program to find the node at which the 
intersection of two singly linked lists begins.

e.g.
A = [1,2,3,4,5]
B = [0,8,3,7,9]
intersection at 3
'''

class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None


class Solution(object):
	def getIntersectionNode(self, headA, headB):
		p, q = headA, headB
		while p!=q:
			p = p.next if p else headB
			q = q.next if q else headA
		return p

def main():
	a = ListNode(1)
	b = ListNode(2)
	c = ListNode(3)
	a.next = b
	b.next = c

	d = ListNode(0)
	e = ListNode(2)
	f = ListNode(4)
	d.next = e
	e.next = f

	sol = Solution()

	print(sol.getIntersectionNode(a,b))



if __name__ == "__main__":
	main()
=======
'''
Write a program to find the node at which the 
intersection of two singly linked lists begins.

e.g.
A = [1,2,3,4,5]
B = [0,8,3,7,9]
intersection at 3
'''

class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None


class Solution(object):
	def getIntersectionNode(self, headA, headB):
		p, q = headA, headB
		while p!=q:
			p = p.next if p else headB
			q = q.next if q else headA
		return p

def main():
	a = ListNode(1)
	b = ListNode(2)
	c = ListNode(3)
	a.next = b
	b.next = c

	d = ListNode(0)
	e = ListNode(2)
	f = ListNode(4)
	d.next = e
	e.next = f

	sol = Solution()

	print(sol.getIntersectionNode(a,b))



if __name__ == "__main__":
	main()
>>>>>>> b58a368f7589ead8231635cc47bbf3b440c9b049

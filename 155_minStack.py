'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''


class MinStack:
	def __init__(self):
		self.stack = []


	def push(self, x:int)->None:
		self.stack.append(x)

	def pop(self)->None:
		self.stack.pop()

	def top(self) ->int:
		return self.stack[-1]

	def getMin(self)->int:
		return min(self.stack)


def main():
	sol = MinStack()
	input = [-3,-2,-1,0,1,2,3]
	for x in input:
		sol.push(x)

	sol.pop()
	print(f"Top of stack is: {sol.top()}")
	print(f"Minimum is: {sol.getMin()}")


if __name__ == "__main__":
	main()
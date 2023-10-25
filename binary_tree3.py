# Python program to print level
# order traversal using Queue


# A node structure
class Node:

	# A utility function to create a new node
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None


# Iterative Method to print the
# height of a binary tree
def printLevelOrder(root):

	# Base Case
	if root is None:
		return

	# Create an empty queue
	# for level order traversal
	queue = []

	# Enqueue Root and initialize height
	queue.append(root)

	while(len(queue) > 0):

		# Print front of queue and
		# remove it from queue
		print(queue[0].data, end=" ")
		node = queue.pop(0)

		# Enqueue left child
		if node.left is not None:
			queue.append(node.left)

		# Enqueue right child
		if node.right is not None:
			queue.append(node.right)


# Driver Program to test above function
if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	print("Level Order Traversal of binary tree is -")
	printLevelOrder(root)


# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

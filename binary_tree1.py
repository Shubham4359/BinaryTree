class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def print_tree(root):
    if root is None:
        return
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)
    
if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	print_tree(root)
	

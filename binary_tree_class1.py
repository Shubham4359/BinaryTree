class Node:
    def __init__(self,key):
        # data , left child , right child
        self.val=key
        self.left=None
        self.right=None

def postorder_print(root):
    #basecase
    if root is None:
        return
    #mainrecursive_case
    postorder_print(root.left)
    postorder_print(root.right)
    print(root.val)

def inorder_print(root):
    #basecase
    if root is None:
        return
    #mainrecursive case
    inorder_print(root.left)
    print(root.val)
    inorder_print(root.right)
    
def preorder_print(root):
    #basecase
    if root is None:
        return
    #mainrecursive case 
    print(root.val)
    preorder_print(root.left)
    preorder_print(root.right)
    
    
if __name__ == '__main__':
    root=Node(1)
    root.left=Node(3)
    root.right=Node(2)
    root.left.right=Node(4)
    root.left.left=Node(5)
    preorder_print(root)
    print("preorder is done")
    postorder_print(root)
    print("postorder is done")
    inorder_print(root)
    print("inorder is done")
    
    
    
    

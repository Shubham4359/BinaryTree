class Node:
    def __init__(self,key):
        # data , left child , right child
        self.val=key
        self.left=None
        self.right=None

def Levelk(root,cur_level,expected_level):
    if root is None:
        return
    if cur_level == expected_level:
        print(root.val)
        return
    Levelk(root.left,cur_level+1,expected_level)
    Levelk(root.right,cur_level+1,expected_level)

def Height(root):
    #basecase
    if root is None:
        return 0
    return max(Height(root.left),Height(root.right))+1
    
def bfs(root):
    queue=[]
    queue.append(root)
    while(len(queue)>0):
        print(queue[0].val,end=" ")
        cur_node=queue.pop(0)
        if cur_node.left is not None:
            queue.append(cur_node.left)
        if cur_node.right is not None:
            queue.append(cur_node.right)
            

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
    root.right.left=Node(7)
    h=Height(root)
    #for i in range(1,h+1):
    #    Levelk(root,1,i)
    bfs(root)
    

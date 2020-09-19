class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
def is_Complete(root,n,index):
    if root is None:
        return True
    if index>=n:
        return False   
    return is_Complete(root.left,n,2*index+1) and is_Complete(root.right,n,2*index+2)
def count(root):
    if root is None:
        return 0
    return (1+count(root.left)+count(root.right))

root=Node(1,left=Node(2,left=Node(4),right=Node(5)),right=Node(3))
ind=0
if is_Complete(root,count(root),ind):
    print("Your tree is a Complete Binary Tree")
else:
    print("Not a binary Complete Binary tree ")
root.right.left=Node(6)
if is_Complete(root,count(root),ind):
    print("Your tree is a Complete Binary Tree")
else:
    print("Not a binary Complete Binary tree ")
root.left.left.left=Node(7)
if is_Complete(root,count(root),ind):
    print("Your tree is a Complete Binary Tree")
else:
    print("Not a binary Complete Binary tree ")
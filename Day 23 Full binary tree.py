class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
def is_Full(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is not None and root.right is not None:
        return (is_Full(root.left)) and (is_Full(root.right))        
    return False
root=Node(1,left=Node(2,left=Node(4),right=Node(5)),right=Node(3))
if is_Full(root):
    print("Your tree is a Full Binary Tree")
root.left.left.left=Node(6)
if is_Full(root):
    print("Your tree is a Full Binary Tree")
else:
    print("Not a binary tree")
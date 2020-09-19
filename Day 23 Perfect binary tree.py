class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
def depth(root):
    d=0
    while(root):
        d+=1
        root=root.left
    return d
def is_perfect(root,d,level=0):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return (d==level+1)
    if root.left is None and root.right is None:
        return False
    return is_perfect(root.left,d,level+1) and is_perfect(root.right,d,level+1)

root=Node(1,left=Node(2,left=Node(4),right=Node(5)),right=Node(3))
if is_perfect(root,depth(root)):
    print("Your tree is a Perfect Binary Tree!!!")
else:
    print("Not a Perfect Binary tree ")
root.right.left=Node(6)
root.right.right=Node(7)
if is_perfect(root,depth(root)):
    print("Your tree is a Perfect Binary Tree!!!")
else:
    print("Not a Perfect Binary tree ")
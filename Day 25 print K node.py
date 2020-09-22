class Node:
    def __init__(self,data,right=None,left=None):
        self.data=data
        self.right=right
        self.left=left
def printknode(root,k):
    if root is None:
        return None
    if k==0:
        print(root.data,end="--")
    else:
        printknode(root.left,k-1)
        printknode(root.right,k-1)

root=Node(1,right=Node(3,right=Node(7),left=Node(6)),left=Node(2,right=Node(5),left=Node(4)))
printknode(root,2)
print()
printknode(root,1)
print()
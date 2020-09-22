class Node:
    def __init__(self,data,right=None,left=None):
        self.data=data
        self.right=right
        self.left=left
def Heightnode(root):
    if root is None:
        return 0
    else:
        l=1+Heightnode(root.left)
        r=1+Heightnode(root.right)
    return max(l,r)

root=Node(1,right=Node(3,right=Node(7),left=Node(6)),left=Node(2,right=Node(5),left=Node(4)))
print("Height of Tree:",Heightnode(root))
root.left.left.left=Node(5)
print("Height of Tree:",Heightnode(root))
root.left.left.left.left=Node(55)
print("Height of Tree:",Heightnode(root))
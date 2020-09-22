class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def SizeOfTree(root):
    if root is None:
        return 0
    else:
        return (1+SizeOfTree(root.left)+SizeOfTree(root.right))

root=Node(1,right=Node(3),left=Node(2,right=Node(5),left=Node(4)))
print("Size of tree is :",SizeOfTree(root))
root.right.right=Node(7)
root.right.left=Node(6)
print("Size of tree is :",SizeOfTree(root))
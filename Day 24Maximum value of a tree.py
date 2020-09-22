class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def MaxOfTree(root):
    if root is None:
        return float('-inf')
    else:
        return max(MaxOfTree(root.left),MaxOfTree(root.right),root.data)

root=Node(1,right=Node(37),left=Node(2,right=Node(55),left=Node(49)))
print("Max of tree is :",MaxOfTree(root))
root.right.right=Node(100)
root.right.left=Node(66)
print("Max of tree is :",MaxOfTree(root))
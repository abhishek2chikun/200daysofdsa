class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end="->")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data,end="->")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end="->")

root=Node(1,right=Node(3),left=Node(2,right=Node(5),left=Node(4)))
'''root=Node(1)
root.right=Node(3)
root.left=Node(2)
root.left.right=Node(5)
root.left.left=Node(4)'''
print("Inorder:")
inorder(root)
print("\npreorder:")
preorder(root)
print("\npostorder:")
postorder(root)
print()
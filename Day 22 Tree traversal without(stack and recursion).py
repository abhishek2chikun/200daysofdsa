class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
def Morris_traversal(root):
    curr=root
    while curr is not None:
        if curr.left is None:
            yield curr.data 
            curr=curr.right
        else:
            pre=curr.left
            while pre.right is not None and pre.right is not curr:
                pre=pre.right
            if pre.right is None:
                pre.right=curr
                curr=curr.left
            else:
                pre.right=None
                yield curr.data 
                curr=curr.right
root=Node(1,right=Node(3),left=Node(2,right=Node(5),left=Node(4)))
print("Inorder:")
for i in Morris_traversal(root):
    print(i,end="->")
print("\n")
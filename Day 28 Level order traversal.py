class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def LeverOrderTraversal(root):
    if root is None:
        return
    q=[];q.append(root)
    while True:
        count=len(q)
        for _ in range(count):
            temp=q.pop(0)
            print(temp.data,end="--")
            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)
        if len(q)==0:
            break
        print()
root=Node(10,left=Node(20,left=Node(40),right=Node(50)),right=Node(30,left=Node(60),right=Node(70)))
LeverOrderTraversal(root)
print()
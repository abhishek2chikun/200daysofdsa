class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
def findpath(root,path,n):
    if root is None:
        return False
    path.append(root.data)
    if root.data==n:
        return True
    if findpath(root.left,path,n) or findpath(root.right,path,n):
        return True
    path.pop()
    return False
def lca(root,n1,n2):
    path1=[]
    path2=[]
    if findpath(root,path1,n1) is False or findpath(root,path2,n2) is False:
        return None
    print(path1,path2)
    for i in range(min(len(path1),len(path2))):
        if path1[i+1]!=path2[i+1]:
            return path1[i]
root=Node(1,right=Node(3,right=Node(7),left=Node(6)),left=Node(2,right=Node(5),left=Node(4)))
print(lca(root,7,5))
print()
print(lca(root,6,7))


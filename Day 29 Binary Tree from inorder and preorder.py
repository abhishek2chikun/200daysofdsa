class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
def printinn(root):
    if root is None:
        return 
    printinn(root.left)
    print(root.data,end="->")
    printinn(root.right)
def BinaryTree(inn,pre,start,end):
    if(start>end):
        return None
    root=Node(pre[BinaryTree.preidx])
    BinaryTree.preidx+=1
    if start==end:
        return root
    idx=Search(inn,start,end,root.data)
    root.left=BinaryTree(inn,pre,start,idx-1)
    root.right=BinaryTree(inn,pre,idx+1,end)
    return root
def Search(arr,st,end,value):
    for i in range(end):
        if arr[i]==value:
            return i

inn=[40,20,50,10,60,30,70]
pre=[10,20,40,50,30,60,70]
BinaryTree.preidx=0
printinn(root=BinaryTree(inn,pre,0,len(inn)-1))
print()
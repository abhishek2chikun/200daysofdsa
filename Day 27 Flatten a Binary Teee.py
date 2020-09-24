class Node:
    def __init__(self,data,left=None,right=None,prev=None,next=None):
        self.left=left
        self.right=right
        self.data=data
        self.prev=prev
        self.next=next

def flatten(root):
    inorderroot=inorder(root,[])
    for i in range(0,len(inorderroot)-1):
        prev=inorderroot[i]
        next=inorderroot[i+1]
        prev.next=next
        next.prev=prev
    printl(inorderroot[0])

def printl(head):
    temp=head
    while temp is not None:
        print(temp.data,end="->")
        temp=temp.next
    print("Null")
    return
    
def inorder(root,array):
    if root is None:
        return
    inorder(root.left,array)
    array.append(root)
    inorder(root.right,array)
    return array    

root=Node(1,right=Node(3),left=Node(2,left=Node(4),right=Node(5)))
print("After Flatting the Binary tree")
flatten(root)

class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
class Inorder():
    def __init__(self):
        self.stack=[]

    def inorder(self,root):
        temp=root
        while True:
            if temp is not None:
                self.stack.append(temp)
                temp=temp.left
            elif(self.stack):
                temp=self.stack.pop()
                print(temp.data,end="->")
                temp=temp.right
            else:
                break
        print()
root=Node(1,right=Node(3),left=Node(2,right=Node(5),left=Node(4)))
x=Inorder()
print("Inorder:")
x.inorder(root)

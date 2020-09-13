#Creating a Stack through array
#Creating stack function
def createstack():
    stack=[]
    return stack
def isEmpty(stack):
    return len(stack)==0
def push(stack,item):
    stack.append(item)
    print(item,"is pushed to you stack:",stack)
def pop(stack):
    if isEmpty(stack)==True:
        print("\nStack is empty,Under FLow")
    else:
        popped=stack.pop()
        print(popped,"is pop out from the stack",stack)
def peek(stack):
    if isEmpty(stack)==True:
        print("\nStack is empty,Under FLow")
    else:
        print("\npeek of stack is",stack[len(stack)-1])
S=createstack()
for i in range(1,10):
    push(S,i*10)
pop(S)
pop(S)
pop(S)
peek(S)
print(isEmpty(S))
#Stack as Linked List
class Node:
    def __init__(self,val=None):
        self.data=val
        self.next=None
class Stack:
    def __init__(self,root=None):
        self.root=None
    def push(self,item):
        item=Node(item)
        item.next=self.root
        self.root=item
        return self.root
    def isEmpty(self):
        return self.root is None
    def pop(self):
        if self.isEmpty is True:
            return "Empty"
        temp=self.root
        self.root=self.root.next
        popped=temp.data 
        return popped
    def peek(self):
        if self.isEmpty is True:
            return "Empty"
        return self.root.data
    def printl(self):
        temp=self.root
        while temp.next is not None:
            print(temp.data,end="->")
            temp=temp.next
s=Stack()
for i in range(10):
    s.push(i*10)
print("\n")
s.printl()
print("\n Popped element is",s.pop())
print("\n Popped element is",s.pop())
print("\n Peek element is:",s.peek())
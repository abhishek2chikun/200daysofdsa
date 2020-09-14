#MixMaxStack Using LinkedList
class Node:
    def __init__(self,val=None):
        self.data=val
        self.next=None
class StackLinkedList:
    def __init__(self,root=None,Min=None,Max=None,pmin=None,pmax=None):
        self.Min=None
        self.Max=None
        self.root=None
        self.pmin=None
        self.pmax=None
    
    def push(self,item):
        item=Node(item)
        if self.root is None:
            self.Min=item
            self.Max=item
            self.pmin=self.Min
            self.pmax=self.Max
        else:
            self.pmin=self.Min
            self.pmax=self.Max
            if (self.Min.data>item.data):
                self.Min=item
            else:
                self.Min=self.Min
            if (self.Max.data<item.data):
                self.Max=item
            else:
                self.Max=self.Max
        item.next=self.root
        self.root=item
        print(item.data,"is Pushed to stack")
        return self.root

    def pop(self):
        if self.root is None:
            return "Stack is Empty"
        self.Min=self.pmin
        self.Max=self.pmax
        temp=self.root
        self.root=self.root.next
        print(temp.data,"is popped out from stack")
    
    def printl(self):
        temp=self.root
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
        print("\n")
    def Mini(self):
        return self.Min.data
    def Maxi(self):
        return self.Max.data

sl=StackLinkedList()
for i in range(1,10):
    sl.push(i*10)
sl.printl()
print("Min of Stack is:",sl.Mini())
print("Max of Stack is:",sl.Maxi())
sl.printl()
sl.pop()
print("Min of Stack is:",sl.Mini())
print("Max of Stack is:",sl.Maxi())
sl.pop()
sl.pop()
sl.printl()


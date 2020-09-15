class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class deque:
    def __init__(self):
        self.head=None
        self.tail=None

    def enqueue(self,element,res="nr"):
        element=Node(element)
        if self.head is None:
            element.next=self.head
            self.head=self.tail=element
            return
        if res=="r":
            x=str(input("From where you want to restrict insertion f:front r:rear---"))
            if  x=="f":
                self.enqueueR(element)
                self.printdq()
            else:
                self.enqueueF(element)
                self.printdq()
        else:
            x=str(input("From where you want to insert f:front r:rear----"))
            if  x=="f":
                self.enqueueF(element)
                self.printdq
            else:
                self.enqueueR(element)
                self.printdq()
        
    def enqueueF(self,element):
        element.next=self.head
        self.head=element
            
    def enqueueR(self,element):
        element.next=None
        self.tail.next=element
        self.tail=element

    def printdq(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
        print("\n")

    def dequeue(self,res="nr"):
        if self.head is None:
            print("Underflow!! No elements to delete")
            return
        if res=="r":
            x=str(input("From where you want to restrict the deletion f:front r:rear---"))
            if  x=="f":
                self.dequeueR()
                self.printdq()
            else:
                self.dequeueF()
                self.printdq()
        else:
            x=str(input("From where you want to delete f:front r:rear----"))
            if  x=="f":
                self.dequeueF()
                self.printdq
            else:
                self.dequeueR()
                self.printdq()
    
    def dequeueF(self):
        self.head=self.head.next
    def dequeueR(self):
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=None
        self.tail=temp 
        
dq=deque()
dq.dequeue()
dq.enqueue(10)
dq.enqueue(20)
dq.enqueue(30,"r")
dq.dequeue()
dq.dequeue("r")
dq.enqueue(50,"r")




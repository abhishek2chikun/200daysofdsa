class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        
class Queue:
    def __init__(self,front=None,rear=None):
        self.front=None
        self.rear=None
    
    def enqueue(self,element):
        element=Node(element)
        if self.front==None:
            self.front=element
            self.rear=element
            print(element.data,"is enqueue to your queue")
        else:
            self.rear.next=element
            self.rear=element
            print(element.data,"is enqueue to your queue")
            return self.front
    
    def dequeue(self):
        if self.front==self.rear:
            print("Under Flow!! No elements")
            return
        temp=self.front
        self.front=self.front.next
        print("dequeue element is:",temp.data)
        return self.front

    def printl(self):
        temp=self.front
        while temp is not self.rear:
            print(temp.data,end="->")
            temp=temp.next
        return self.front
q=Queue()
q.dequeue()
for i in range(1,7):
    q.enqueue(i*10)
q.printl()
print("\n")
q.dequeue()
print("\n")
q.printl()
print("\n")

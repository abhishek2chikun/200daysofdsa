class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=Node

class PriorityQueue:
    def __init__(self):
        self.head=None
        self.tail=None

    def enqueue(self,element):
        element=Node(element)
        if self.head is None:
            element.next=self.head
            self.head=self.tail=element
        
        elif self.head.data < element.data:
            element.next=self.head
            self.tail=self.head
            self.head=element
        
        elif self.tail.data > element.data:
            element.next=None
            self.tail.next=element
            self.tail=element

        else:
            p=self.head
            temp=self.head.next
            while temp is not None:
                if temp.data<element.data:
                    break
                p=p.next
                temp=temp.next
            element.next=temp
            p.next=element

    def dequeue(self,p="h"):
        if self.head is None:
            print("Empty")
        elif p=="h":
            temp=self.head
            self.head=self.head.next
            print("dequeue element is:",temp.data)

        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=None
            print("dequeue element is:",temp.data)
            self.tail=temp

    def printpq(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
        print("\n")

pq=PriorityQueue()
for i in range(5,9):
    pq.enqueue(i*5)
pq.printpq()
pq.dequeue("l")
pq.printpq()
pq.dequeue("h")
pq.printpq()
for i in range(10,14):
    pq.enqueue(i*10)
pq.printpq()


            
    

class circularqueue:
    def __init__(self,K):
        self.K=K
        self.queue=[None]*K
        self.head=self.tail=-1

    def enqueue(self,element):
        if (self.tail+1)%self.K==self.head:
            print("Overflow!!!!!!!Queue is Full\n")
        elif (self.head==-1):
            self.head=0
            self.tail=0
            self.queue[self.tail]=element
        else:
            self.tail=(self.tail+1) % self.K
            self.queue[self.tail]=element

    def dequeue(self):
        if self.head==-1:
            print("Underflow!!!!Queue is Empty\n")
        elif self.head==self.tail:
            self.head=-1
            self.tail=-1
        else:
            temp=self.head
            self.head=(self.head+1) % self.K 
            return temp

    def printcq(self):
        if self.head==-1:
            print("No element in queue")
        elif (self.tail>=self.head):
            for i in range(self.head,self.tail+1):
                print(self.queue[i],end="--")
            print("\n")
        else:
            for i in range(self.head,self.K):
                print(self.queue[i],end="--")
            for i in range(0,self.tail+1):
                print(self.queue[i],end="--")
            print("\n")

cq=circularqueue(5)
cq.dequeue()
for i in range(5):
    cq.enqueue(i)
cq.printcq()
cq.dequeue()
cq.enqueue(100)
cq.printcq()
cq.enqueue(500)
cq.dequeue()
cq.enqueue(500)
cq.printcq()
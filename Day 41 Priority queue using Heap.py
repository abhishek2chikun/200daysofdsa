class Node:
    def __init__(self,value,priority):
        self.value=value
        self.priority=priority
class Priority_Queue:
    def __init__(self):
        self.pq=[]
        self.length=len(self.pq)

    def HeapUp(self):
        curr=self.length-1
        while curr>0:
            parent=(curr-1)//2
            if self.pq[curr].priority < self.pq[parent].priority:
                self.pq[curr],self.pq[parent]=self.pq[parent],self.pq[curr]
                curr=parent
            else:
                break
    def HeapDown(self):
        curr=0
        leftchild=2*curr+1
        rightchild=2*curr+2
        while leftchild<=self.length-1:
            swapidx=curr
            if self.pq[leftchild].priority < self.pq[swapidx].priority:
                swapidx=leftchild
            if rightchild<self.length and self.pq[rightchild].priority < self.pq[swapidx].priority:
                swapidx=rightchild
            if swapidx==curr:
                break
            self.pq[curr],self.pq[swapidx]=self.pq[swapidx],self.pq[curr]
            curr=swapidx
            leftchild=2*curr+1
            rightchild=2*curr+2

    def insert(self,value,priority):
        x=Node(value,priority)
        self.pq.append(x)
        self.length+=1
        self.HeapUp()

    def remove(self):
        removed=self.pq[0]
        self.pq[0]=self.pq[self.length-1]
        self.pq.pop()
        self.length-=1
        self.HeapDown()
        return removed.value    
    
pq=Priority_Queue()
pq.insert("A",50)
pq.insert("B",1)
pq.insert("C",10)
pq.insert("Day 41",41)
pq.insert("Z",5)
pq.insert("200 days of DSA",200)
print([pq.pq[i].value for i in range(len(pq.pq))])
for i in range(pq.length):
    print(pq.remove())

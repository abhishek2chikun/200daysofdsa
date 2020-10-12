class Continous_Median:
    def __init__(self,array1,array2):
        self.smaller=Heap(Max_Heap,array1)
        self.grater=Heap(Min_Heap,array2)
        self.median=None

    def insert(self,value):
        if not self.smaller.length or value<self.smaller.peek():
            self.smaller.Insert_heap(value)
        else:
            self.grater.Insert_heap(value)
        self.rebalance()
        print("\t\tMedian is:",self.Median());
        print("Smaller aka Max_Heap is:",self.smaller.heap);print("Larger aka Min_Heap is:",self.grater.heap)
    
    def rebalance(self):
        if self.smaller.length-self.grater.length==2:
            self.grater.Insert_heap(self.smaller.remove())

        elif self.grater.length-self.smaller.length==2:
            self.smaller.Insert_heap(self.grater.remove())
    
    def Median(self):
        if self.smaller.length==self.grater.length:
            self.median=(self.smaller.peek()+self.grater.peek())/2
        elif self.smaller.length<self.grater.length:
            self.median=self.grater.peek()
        else:
            self.median=self.smaller.peek()
        return self.median
class Heap:
    def __init__(self,fun,array):
        self.heap=self.buildheap(array)
        self.MinorMax=fun
        self.length=len(self.heap)
    
    def buildheap(self,array):
        level=(len(array)-1)//2
        for curr in reversed(range(level)):
            self.heapDown(curr,len(array)-1,array)
        return array

    def heapDown(self,curr,end,array):
        left=curr*2+1
        while left<=end:
            right=curr*2+2 if curr*2+2<=end else -1
            if right!=-1 :
                if self.MinorMax(array[right],array[left]):
                    toswap=right
                else:
                    toswap=left
            else:
                toswap=left
            if self.MinorMax(array[right],array[left]):
                self.swap(curr,toswap,array)
                curr=toswap
                left=curr*2+1
            else:
                return

    def heapUp(self,curr,array):
        parent=(curr-1)//2 if (curr-1)//2>0 else 0
        while curr>0:
            if self.MinorMax(array[curr],array[parent]):            
                self.swap(curr,parent,array)
                curr=parent
                parent=(curr-1)//2
            else:
                return

    def Insert_heap(self,value):
        self.heap.append(value)
        self.length+=1
        self.heapUp(self.length-1,self.heap)
    
    def remove(self):
        popped=self.heap.pop(0)
        self.length-=1
        self.heapDown(0,self.length-1,self.heap)
        return popped

    def swap(self,x,y,array):
        array[x],array[y]=array[y],array[x]

    def peek(self):
        return self.heap[0]

def Min_Heap(a,b):
        return a<b
def Max_Heap(a,b):
        return a>b

array1,array2=list(),list()
c=Continous_Median(array1,array2)
for _ in range(int(input("Enter the no. of times you want to insert values:"))):
    c.insert(int(input("Enter the Number:")))

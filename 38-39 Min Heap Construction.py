class Heap:
    def __init__(self,array):
        self.heap=self.buildheap(array)
    
    def buildheap(self,array):
        level=(len(array)-1)//2
        for curr in reversed(range(level)):
            self.heapDown(curr,len(array)-1,array)
        return array
    def heapDown(self,curr,end,array):
        left=curr*2+1
        while left<=end:
            right=curr*2+2 if curr*2+2<=end else -1
            if right!=-1 and array[right]<array[left]:
                toswap=right
            else:
                toswap=left
            if array[toswap]<array[curr]:
                self.swap(curr,toswap,array)
                curr=toswap
                left=curr*2+1
            else:
                break
    def heapUp(self,curr,array):
        parent=(curr-1)//2
        while parent<curr and curr!=0:
            if array[curr]<array[parent]:
                self.swap(curr,parent,array)
                curr=parent
                parent=(curr-1)//2
            else:
                break

    def insert(self,value):
        self.heap.append(value)
        self.heapUp(len(self.heap)-1,self.heap)
        return self.heap
    
    def remove(self):
        self.swap(0,len(self.heap)-1,self.heap)
        popped=self.heap.pop()
        self.heapDown(0,len(self.heap)-1,self.heap)
        return self.heap

    def swap(self,x,y,array):
        array[x],array[y]=array[y],array[x]
    def peek(self):
        return self.heap[0]
min_heap=Heap(array=[3,65,2,4,33,54,45])
print("Heap:",min_heap.heap)
print("Peek:",min_heap.peek())
print("Insert 1:",min_heap.insert(1))
print("Insert 50:",min_heap.insert(50))
print("After Remove:",min_heap.remove())
print("After Remove:",min_heap.remove())

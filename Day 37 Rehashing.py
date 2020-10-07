class HashNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
class Map:
    def __init__(self,bucket_size):
        self.bucket_size=bucket_size
        self.bucket=[None for _ in range(bucket_size)]
        self.count=0
    def rehash(self):
        temp=self.bucket
        self.bucket_size=self.bucket_size*2
        self.bucket=[None for _ in range(self.bucket_size)]
        self.count=0
        for head in temp:
            while head is not None:
                self.insert(head.key,head.value)
                head=head.next      
    
    def insert(self,Key,value):
        hc=hash(Key)
        index=(abs(hc)%self.bucket_size)
        head=self.bucket[index]
        while head is not None:
            if head.key==Key:
                head.value=value
                return
            head=head.next
        head=self.bucket[index]
        new_node=HashNode(Key,value)
        new_node.next=head
        self.bucket[index]=new_node
        self.count+=1
        if (self.count/self.bucket_size)>=0.7:
            self.rehash()
    def getvalue(self,Key):
        hc=hash(Key)
        index=(abs(hc)%self.bucket_size)
        head=self.bucket[index]
        while head is not None:
            if head.key==Key:
                return f"Value on key {Key} is {head.value}"
            head=head.next
        return None
    def remove(self,Key):
        hc=hash(Key)
        index=(abs(hc)%self.bucket_size)
        head=self.bucket[index]
        prev=None
        while head is not None:
            if head.key==Key:
                if prev is None:
                    self.bucket[index]=None
                else:
                    prev.next=head.next
                    head.next=None
                self.count-=1
                return 
            prev=head
            head=head.next
    def NoofNode(self):
        return self.count
m=Map(5)
print("Size of Bucket before Rehasing",m.bucket_size)
for i in range(50):
    m.insert("abc"+str(i),i*10)
print("Size of Bucket after rehashing",m.bucket_size)
print("No. of Node:",m.NoofNode())
print(m.getvalue("abc10"))
print(m.getvalue("abc0"))
print(m.getvalue("abc28"))
for i in range(0,50,5):
    m.remove("abc"+str(i))
print("After Removing")
print("No. of Node:",m.NoofNode())
print(m.getvalue("abc10"))
print(m.getvalue("abc0"))
print(m.getvalue("abc28"))

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
    def insert(self,Key,value):
        hc=hash(Key)
        index=(abs(hc)%self.bucket_size)
        head=self.bucket[index]
        while head is not None:
            if head.key==Key:
                head.value=value
                return
            head=head.next
        new_node=HashNode(Key,value)
        new_node.next=head
        self.bucket[index]=new_node
        self.count+=1
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
m=Map(10)
m.insert("Day",0)
m.insert("36",36)
m.insert("by",50)
m.insert("200",100)
m.insert("days",200)
m.insert("of",300)
m.insert("DSA",400)
print("Size of Node is:",m.NoofNode())
print(m.getvalue("DSA"))
m.remove("Day")
print("Size of Node is:",m.NoofNode())
print(m.getvalue("Day"))
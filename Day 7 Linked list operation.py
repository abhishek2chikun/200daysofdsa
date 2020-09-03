class node:
    def __init__(self, data):
        self.data = data  
        self.next = None  
class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def traverse(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def insertAtBeginning(self, data):
        new_node = node(data)

        new_node.next = self.head
        self.head = new_node
        
    def insertAtEnd(self,data):
        last_node=node(data)
        if self.head==None:
            self.head=last_nodel
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=last_node
        
    def insertAtposition(self,pre,data):
        if pre is None:
            print("No node exist as:",pre)
            return
        pos_node=node(data)
        pos_node.next=pre.next
        pre.next=pos_node

    def deleteAtpos(self,pos):
        if self.head==None:
            return
        temp=self.head
        if pos==1:
            self.head=temp.next
            temp=None
        for i in range(pos-1):
            temp=temp.next
            if temp == None:
                break
        if temp == None:
            return
        if temp.next == None:
            return
        next=temp.next.next
        temp.next=None
        temp.next=next
        
    def deleteAtkey(self,key):
        if self.head==None:
            return
        temp=self.head
        if (temp.data==key):
            self.head=temp.next
            temp=None
            return
        while(temp):
            if (temp.data==key):
                break
            pre=temp
            temp=temp.next
        if temp==None:
            return
        pre.next=temp.next
        temp=None


l=LinkedList()
l.head=node(1)
a=node(2)
b=node(3)
c=node(4)
l.head.next=a
a.next=b
b.next=c
print("Your linked list")
l.traverse()
print("Insertion at begging")
l.insertAtBeginning(100)
l.traverse()
print("Insertion at end")
l.insertAtEnd(200)
l.traverse()
print("Insertion at position")
l.insertAtposition(b,300)
l.traverse()
print("linked list after deletion of node at position 6")
l.deleteAtpos(4)
l.traverse()
print("linked list after deletion of node having key 200")
l.deleteAtkey(200)
l.traverse()
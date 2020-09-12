class Node:
    def __init__(self, val=None):
        self.data = val
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self,node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail,node)
    def insertBefore(self, node, nodetoInsert):
        #nodetoInsert=Node(nodetoInsert)
        if nodetoInsert == self.head or nodetoInsert == self.tail:
            return
        self.remove(nodetoInsert)
        nodetoInsert.prev = node.prev
        nodetoInsert.next = node
        if nodetoInsert.prev is None:
            self.head = nodetoInsert
        else:
            node.prev.next = nodetoInsert
        node.prev=nodetoInsert

    def insertAfter(self,node,nodetoInsert):
        #nodetoInsert=Node(nodetoInsert)
        if nodetoInsert==self.head or nodetoInsert==self.tail:
            return
        self.remove(nodetoInsert)
        nodetoInsert.prev=node
        nodetoInsert.next=node.next
        if nodetoInsert.next is None:
            self.tail=nodetoInsert
        else:
            node.next.prev=nodetoInsert
        node.next=nodetoInsert

    def insertAtpos(self,pos,nodetoInsert):
        if pos==1:
            self.setHead(nodetoInsert)
            return
        counter=1
        node=self.head
        while node.next is not None and counter!=pos:
            counter+=1
            node=node.next
        if node is not None:
            self.insertBefore(node,nodetoInsert)
        else:
            self.setTail(nodetoInsert)
    def remove(self,node):
        if(node==self.head):
            self.head=self.head.next
        if(node==self.tail):
            self.tail=self.tail.prev
        self.removeNodeBinding(node)
    def removeNodeBinding(self,node):
        if node.prev is not None:
            node.prev.next=node.next
        if node.next is not None:
            node.next.prev=node.prev
        node.next=None
        node.prev=None
    def containsvalue(self,value):
        node=self.head
        while node is not None and node.data!=value:
            node=node.next
        return node is not None
    def printlist(self,node):
        print("\nDouble Linked list\n")
        while node is not None:
            print(node.data,end="<->")
            last = node
            node = node.next
        print("\nReverse\n")
        while (last is not None):
            print(last.data,end="<->")
            last = last.prev


Dll=DoubleLinkedList()
Dll.head=Node(10)
one=Node(20)
two=Node(30)
three=Node(40)
Dll.head.next=one
one.prev=Dll.head
one.next=two
two.prev=one
two.next=three
three.prev=two
Dll.printlist(Dll.head)
print("\nAfter Removal of node two")
Dll.remove(two)
Dll.printlist(Dll.head)
print("\nIsertion of node after node one")
Dll.insertAfter(one,Node(100))
Dll.printlist(Dll.head)
print("\nInsertion of node before node three\n")
Dll.insertBefore(three,Node(500))
Dll.printlist(Dll.head)
print("\nInsert at position")
Dll.insertAtpos(three,Node(800))
Dll.printlist(Dll.head)
print("\nSet head")
Dll.setHead(Node(5))
Dll.printlist(Dll.head)
print("\nSet Tail")
Dll.setTail(Node(20))
Dll.printlist(Dll.head)
Dll.setTail(Node(555))
Dll.printlist(Dll.head)
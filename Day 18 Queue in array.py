class Arrayqueue:
    def __init__(self):
        self.queue=[]

    def enqueue(self,element):
        self.queue.append(element)
        print("{0} is enqueue....Now your queue:{1}".format(element,self.queue))

    def dequeue(self):
        if len(self.queue)==0:
            print("UnderFlow !!No element in queue")
        else:
            x=self.queue.pop(0)
            print("{0} is dequeue .... Now your queue:{1}".format(x,self.queue))
      
q=Arrayqueue()
for i in range(1,10):
    q.enqueue(i*5)
q.dequeue()
q.dequeue()
q.dequeue()

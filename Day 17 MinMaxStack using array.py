#Using Array MixMaxStack
class minmaxstack:
    def __init__(self):
        self.minmax=[]
        self.stack=[]
    def peek(self):
        return self.stack[len-1]
    def pop(self):
        if len(self.stack)==0:
            print("Stack is empty Insert Item")
        else:
            self.minmax.pop()
            x=self.stack.pop()
            print("{0} is popped out of your stack,\nYour current stack is {1}".format(x,self.stack))  
    def push(self,item):
        newminmax={"min":item,"max":item}
        if len(self.minmax):
            lastminmax=self.minmax[(len(self.minmax)-1)]
            newminmax["min"]=min(lastminmax["min"],item)
            newminmax["max"]=max(lastminmax["max"],item)
        self.minmax.append(newminmax)
        self.stack.append(item)
        print("Your stack is:",self.stack)
    def minstack(self):
        return self.minmax[len(self.minmax)-1]["min"] 
    def maxstack(self):
        return self.minmax[len(self.minmax)-1]["max"] 

s=minmaxstack()
s.pop()
for i in range(1,6):
    s.push(i*10)
print("Min of stack is:",s.minstack())
print("Max of stack is:",s.maxstack())
s.pop()
s.pop()
print("Min of stack is:",s.minstack())
print("Max of stack is:",s.maxstack())

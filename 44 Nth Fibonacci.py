import time
#Using Reursion
def Fibo(x):
    if x==1 or x==2:
        return x-1
    else:
        return Fibo(x-1)+Fibo(x-2)
print("\n\t\t---Fibonacci using Recursion---\n\tTime Complexity:O(2pow(N))\tSpace Complexity:O(N)")
start=time.time()
for i in range(1,int(input("Enter the range:"))):
    print(Fibo(i),end="\t")
print()
time.sleep(0)
end=time.time()
print("Time Taken for Recursion:",end-start)
print()




#Using Hashing
def FiboHash(x,memory={1:0,2:1}):
    if x in memory:
        return memory[x]
    else:
        memory[x]=FiboHash(x-1,memory)+FiboHash(x-2,memory)
        return memory[x]
print("\n\t\t---Fibonacci using Hashing---\n\tTime Complexity:O(N)\tSpace Complexity:O(N)")
start=time.time()
for i in range(1,int(input("Enter the range:"))):
    print(FiboHash(i),end="\t")
print()
time.sleep(0)
end=time.time()
print("Time Taken for Hashing:",end-start)
print()



#Using Iteration
def FiboIter(x):
    arr=[0,1]
    count=3
    while count<=x:
        temp=arr[0]+arr[1]
        arr[0]=arr[1]
        arr[1]=temp
        count+=1
    return arr[1] if x>1 else arr[0]
print("\n\t\t---Fibonacci using Iteration---\n\tTime Complexity:O(N)\tSpace Complexity:O(1)")
start=time.time()
for i in range(1,int(input("Enter the range:"))):
    print(FiboIter(i),end="\t")
print()
time.sleep(0)
end=time.time()
print("Time Taken for Iteration:",end-start)
print()
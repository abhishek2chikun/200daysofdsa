def Three_Largest(x:list)->list:
    Largest=[None,None,None]
    for num in x:
        findlargest(Largest,num)
    return Largest
def findlargest(Largest,num):
    if Largest[2] is None or num>Largest[2]:
        shift(Largest,num,2)
    elif Largest[1] is None or num>Largest[1]:
        shift(Largest,num,1)
    elif Largest[0] is None or num>Largest[0]:
        shift(Largest,num,0)
def shift(Largest,num,idx):
    for i in range(idx+1):
        if i==idx:
            Largest[i]=num
        else:
            Largest[i]=Largest[i+1]

            
import random
for _ in range(int(input("Enter Number of times:"))):
    x=[random.randrange(-20,100) for i in range(10)]
    print("\nList of Number is:",x)
    print("Three Largest Number is :",Three_Largest(x))

def Createstack():
    stack=[]
    return stack
def BalanceBracket(stack,string):
    Opening="([{"
    Closing="}])"
    Matching={")":"(","]":"[","}":"{"}
    for char in string:
        if char in Opening:
            stack.append(char)
        elif char in Closing:
            if len(stack)==0:
                return False
            if stack[-1]==Matching[char]:
                stack.pop()
            else:
                return False
    return len(stack)==0

for _ in range(int(input("Enter no. of times:"))):
    x=str(input("Enter your Bracket: "))
    BB=Createstack()
    if BalanceBracket(BB,x)==True:
        print("\n\tYes!!! Your is having balance bracket")
    else:
        print("\n\tSorry Bracket are not balanced")




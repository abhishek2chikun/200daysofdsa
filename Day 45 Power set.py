def powerset(x:list)->list:
    sub=[[]]
    for ele in x:
        for i in range(len(sub)):
            curr=sub[i]
            sub.append(curr+[ele])
    return sub
    
print("Power Set of 123:",powerset((1,2,3)))
print("\nPower set of 12:",powerset((1,2)))
print("\nPower set of 5,6,7:",powerset((5,6,7)))
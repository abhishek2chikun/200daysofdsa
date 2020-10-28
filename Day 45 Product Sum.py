def prosum(Array,mul=1):
    Sum=0
    for elements in Array:
        if type(elements) is list:
            Sum+=prosum(elements,mul+1)
        else:
            Sum+=elements
    return mul*Sum

print("Product Sum is:",prosum([[[[10]]]]))
print("Product Sum is:",prosum([1,10,20,[50,[-100,50],200],500]))
print("Product Sum is:",prosum([10,12,55,[20,30,95,[-20,10],10],[[[-10]]]]))
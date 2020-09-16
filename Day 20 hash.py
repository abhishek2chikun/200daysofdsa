
hashTable=[[],]*10

def checkprime(n):
    if n==1 or n==0:
        return 0
    else:
        for i in range(2,n//2):
            if n % i==0:
                return 0
    return 1

def getPrime(n):
    if n % 2 == 0:
        n = n + 1
    while not checkprime(n):
        n += 2
    return n

def hashfun(key):
    capacity=getPrime(10)
    return key % capacity

def insertData(key, data):
    index = hashfun(key)
    hashTable[index] = [key, data]

def removeData(key):
    index = hashfun(key)
    hashTable[index] = []

insertData(123, "200")
insertData(432, "days")
insertData(213, "of")
insertData(654, "DSA")
print(hashTable,"\n")
removeData(123)
print(hashTable,"\n")
insertData(321,"20/200")
print(hashTable)
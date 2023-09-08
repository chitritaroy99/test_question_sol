def matchingStrings(stringList, queries):
    c=0
    arr=[]
    for i in queries:
        for j in stringList:
            if i==j:
                c=c+1
        arr.append(c)
        c=0
    return arr

#driver code
stringList=[]
queries=[]
n=int(input())

for i in range (0,n) :  
    a = input()
    stringList.append(a) 

m=int(input())
for i in range (0,m) :  
    b = input()
    queries.append(b)
    
print(matchingStrings(stringList,queries))
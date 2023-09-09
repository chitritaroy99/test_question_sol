def missingnum(arr):
    n=len(arr)  
    s1=0
    for i in arr:
        s1=s1+i
        #add all elements on the given array len n
    n=n+1     
    #one array missing . main array n+1
    s2=(n*(n+1))//2 
    #add all elements main array

    ans=s2-s1 
    #minus
    return ans


 

lst=[]
n=int(input("No of integers : "))

for i in range(n): 
    ele=int(input())
    lst.append(ele)

print("Missing Number is: ",missingnum(lst))

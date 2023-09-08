def missingnum(arr):
    n=len(arr)  
    s1=0
    for i in arr:
        s1=s1+i
    n=n+1        
    s2=(n*(n+1))//2 

    ans=s2-s1  
    return ans

lst=[]
n=int(input("No of integers : "))

for i in range(n): 
    ele=int(input())
    lst.append(ele)

print("Missing Number is: ",missingnum(lst))
def getNode(head, p):
    # Write your code here
    a=b=head
    c=p
    
    while(c>0 and b):
        b=b.next
        c=c-1
        
    while(b and b.next):
        a=a.next
        b=b.next
        
        
    return a.data
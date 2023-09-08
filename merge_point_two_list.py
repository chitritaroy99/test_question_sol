def findMergeNode(head1, head2):
    a=head1
    b=head2
    c1=0
    c2=0
    while(a.next):
        c1=c1+1
        a=a.next
        
    while(b.next):
        c2=c2+1
        b=b.next      
        
    m=abs(c1-c2)
    
    a=head1
    b=head2
     
    if(c1>=c2):
        while(m>0):
            a=a.next
            m=m-1
            
        while(a!=b):
            a=a.next
            b=b.next
        return a.data
            
            
    elif(c2>c1):
        while(m>0):
            b=b.next
            m=m-1
            
        while(a!=b):
            a=a.next
            b=b.next 
            
        return a.data 
def has_cycle(head):
    a=head
    b=head
    while(b and b.next):
        a=a.next
        b=b.next.next
        if (a==b):
            return 1
        
    return 0   
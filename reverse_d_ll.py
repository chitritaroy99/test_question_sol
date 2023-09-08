def reverse(head):
    # Write your code here
    while (head.next):
        head.next,head.prev=head.prev,head.next
        head=head.prev
        
    head.next,head.prev=head.prev,head.next 
        
    return head


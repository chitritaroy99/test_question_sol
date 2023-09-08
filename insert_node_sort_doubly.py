def sortedInsert(head, data):
   
    # Write your code here
    temp = DoublyLinkedListNode(data)
    if head==None:
        return temp
    
    curr = head
    if data<=curr.data:
        temp.next = curr
        curr.prev = temp
        temp.prev = None
        return temp
        
    while curr.next!=None and curr.next.data<data:
        curr = curr.next
    
    if curr.next==None:
        curr.next = temp
        temp.prev = curr
        temp.next = None
        
    else:
        temp.next = curr.next
        curr.next.prev = temp
        curr.next = temp
        temp.prev = curr
    
    return head 


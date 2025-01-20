class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        n=0
        temp=head
        while temp!=None:
            n+=1
            temp=temp.next
        k=k%n
        if k==0:
            return head
        ptr=head
        for i in range(k-1):
            ptr=ptr.next
        newTail=ptr
        newHead=ptr.next
        newTail.next=None
        ptr=newHead
        while ptr.next!=None:
            ptr=ptr.next
        ptr.next=head
        return newHead

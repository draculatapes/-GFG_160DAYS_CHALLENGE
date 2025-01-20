class Solution:
    def sortedMerge(self,head1, head2):
        # code here
        newHead=Node(0)
        tail=newHead
        
        while head1!=None and head2!=None:
            if head1.data<head2.data:
                tail.next=head1
                tail=tail.next
                head1=head1.next
                tail.next=None
            else:
                tail.next=head2
                tail=tail.next
                head2=head2.next
                tail.next=None
        if head1!=None:
            tail.next=head1
        if head2!=None:
            tail.next=head2
        return newHead.next

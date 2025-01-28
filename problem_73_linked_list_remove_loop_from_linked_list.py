class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        fast=head
        slow=None
        while fast!=None and fast.next!=None:
            if slow==None:
                fast=head
                slow=head
            else:
                if slow==fast:
                    break
            slow=slow.next
            fast=fast.next.next
        if fast==None or fast.next==None:
            return head
        if slow==head:
            ptr=head
            while ptr.next!=head:
                ptr=ptr.next
            ptr.next=None
            return head
        ptr=head
        prev=slow
        
        while ptr!=slow:
            prev=slow
            slow=slow.next
            ptr=ptr.next
        prev.next=None
        return head

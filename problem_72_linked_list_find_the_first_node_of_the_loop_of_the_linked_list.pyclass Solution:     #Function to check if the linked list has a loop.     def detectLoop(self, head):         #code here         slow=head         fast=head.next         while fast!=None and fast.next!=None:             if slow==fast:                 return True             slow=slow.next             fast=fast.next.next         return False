class Solution:
    def findFirstNode(self, head):
        #code here
        slow=None
        fast=head
        while fast!=None and fast.next!=None:
            if slow==None:
                slow=head
                fast=head
            else:
                if slow==fast:
                    break
            slow=slow.next
            fast=fast.next.next
        if fast==None or fast.next==None:
            return None
        ptr=head
        while ptr!=slow:
            slow=slow.next
            ptr=ptr.next
        return ptr

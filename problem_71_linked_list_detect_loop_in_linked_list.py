class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        slow=head
        fast=head.next
        while fast!=None and fast.next!=None:
            if slow==fast:
                return True
            slow=slow.next
            fast=fast.next.next
        return False
        

class Solution:
    def reverseList(self, head):
        # Code herer
        revHead=None
        while head!=None:
            next_head=head.next
            head.next=revHead
            revHead=head
            head=next_head
        return revHead

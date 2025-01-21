class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        temp=head
        newHead=Node(0)
        newTail=newHead
        
        
        while temp!=None:
            tempHead=None
            tempTail=temp
            for i in range(k):
                if temp==None:
                    break
                next_node=temp.next
                temp.next=tempHead
                tempHead=temp
                temp=next_node
            newTail.next=tempHead
            newTail=tempTail
            if temp==None:
                break
        return newHead.next

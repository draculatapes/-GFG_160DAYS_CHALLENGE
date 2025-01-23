#Time Complexity: O(N) Space  Complexity: O(N)
class Solution:
    def cloneLinkedList(self, head):
        # code here
        indexOfNode=dict()
        temp=head
        index=0
        while temp!=None:
            indexOfNode[temp]=index
            index+=1
            temp=temp.next
        newHead=Node(0)
        tail=newHead
        nodeAtIndex=dict()
        index=0
        temp=head
        while temp!=None:
            newNode=Node(temp.data)
            nodeAtIndex[index]=newNode
            index+=1
            tail.next=newNode
            tail=tail.next
            temp=temp.next
            
            
        temp1=head
        temp2=newHead.next
        while temp1!=None:
            if temp1.random==None:
                temp2.random=None
            else:
                indexOfRandom=indexOfNode[temp1.random]
                nodeAtRandom=nodeAtIndex[indexOfRandom]
                temp2.random=nodeAtRandom
            temp1=temp1.next
            temp2=temp2.next
        return newHead.next

class Solution:
    def levelOrder(self, root):
        # Your code here
        que=[root]
        res=list()
        while len(que)>0:
            size=len(que)
            lnode=[]
            while size>0:
                node=que.pop(0)
                lnode.append(node.data)
                if node.left!=None:
                    que.append(node.left)
                if node.right!=None:
                    que.append(node.right)
                size-=1
            res.append(lnode)
        return res

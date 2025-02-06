class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        level=0
        que=[root]
        while len(que)>0:
            level+=1
            size=len(que)
            while size>0:
                node=que.pop(0)
                if node.left!=None:
                    que.append(node.left)
                if node.right!=None:
                    que.append(node.right)
                size-=1
        return level-1

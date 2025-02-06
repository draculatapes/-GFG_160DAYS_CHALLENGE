class Solution:
    def diameter(self, root):
        # Your code here
        res=[0]
        def dfs(node,height):
            if node.left==None and node.right==None:
                return 0
            left_sub_height=0
            right_sub_height=0
            if node.left!=None:
                left_sub_height=1+dfs(node.left,height+1)
            if node.right!=None:
                right_sub_height=1+dfs(node.right,height+1)
            res[0]=max(res[0],left_sub_height+right_sub_height)
            return max(left_sub_height,right_sub_height)
        dfs(root,0)
        return res[0]

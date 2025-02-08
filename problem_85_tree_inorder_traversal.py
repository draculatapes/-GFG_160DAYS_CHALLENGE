class Solution:
    def inOrder(self,root):
        # code here
        res=[]
        def inorder(node):
            if node==None:
                return 
            inorder(node.left)
            res.append(node.data)
            inorder(node.right)
        inorder(root)
        return res

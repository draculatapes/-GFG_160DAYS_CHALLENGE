class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        # Code here
        if root==None:
            return None
        temp=root.left
        root.left=self.mirror(root.right)
        root.right=self.mirror(temp)
        return root
    

class Solution:
    
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        self.prev=0
        self.res=True
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            if self.prev!=0 and node.data<=self.prev:
                self.res=False
                return 
            self.prev=node.data
            inorder(node.right)
        inorder(root)
        return self.res

class Solution:
    # Return the kth smallest element in the given BST 
    def kthSmallest(self, root, k): 
        #code here.
        self.res=-1
        self.count=0
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            self.count+=1
            if self.count==k:
                self.res=node.data
                return 
            inorder(node.right)
        inorder(root)
        return self.res

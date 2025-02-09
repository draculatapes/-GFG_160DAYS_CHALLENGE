class Solution:
    #Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root): 
        #Your code here
        M=10000
        self.res=-M
        def maxSum(node):
            if node==None:
                return -M
            lsum=maxSum(node.left)
            rsum=maxSum(node.right)
            curr_res=max(node.data,node.data+lsum+rsum,node.data+lsum,node.data+rsum)
            self.res=max(self.res,curr_res)
            return max(node.data,node.data+lsum,node.data+rsum)
            
        maxSum(root)
        return self.res

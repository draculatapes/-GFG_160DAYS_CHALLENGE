class Solution:
    def sumK(self,root,k):
        # code here
        prefix_pathSum=dict()
        self.res=0
        prefix_pathSum[0]=1
        def traverse(node,curr_sum):
            if node==None:
                return
            curr_sum+=node.data
            needed=curr_sum-k
            if needed in prefix_pathSum and prefix_pathSum[needed]>0:
                self.res+=prefix_pathSum[needed]
            if curr_sum in prefix_pathSum:
                prefix_pathSum[curr_sum]+=1
            else:
                prefix_pathSum[curr_sum]=1
            traverse(node.left,curr_sum)
            traverse(node.right,curr_sum)
            prefix_pathSum[curr_sum]-=1
            if prefix_pathSum[curr_sum]==0:
                del prefix_pathSum[curr_sum]
        traverse(root,0)
        return self.res

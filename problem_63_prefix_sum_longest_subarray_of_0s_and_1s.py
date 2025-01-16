class Solution:
    def maxLen(self, arr):
        # code here
        zeros=0
        ones=0
        prefix_diff=dict()
        prefix_diff[0]=-1
        res=0
        for i in range(len(arr)):
            if arr[i]==0:
                zeros+=1
            else:
                ones+=1
            diff=ones-zeros
            if diff in prefix_diff:
                res=max(res,i-prefix_diff[diff])
            else:
                prefix_diff[diff]=i
        return res

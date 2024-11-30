class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        curr_sum=0
        res=-sys.maxsize
        for ele in arr:
            curr_sum+=ele
            if curr_sum<0:
                res=max(res,curr_sum)
                curr_sum=0
            else:
                res=max(res,curr_sum)
        return res

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        prefix_sum=dict()
        n=len(arr)
        total=0
        res=0
        prefix_sum[0]=-1
        for i in range(n):
            total+=arr[i]
            needed_sum=total-k
            if needed_sum in prefix_sum:
                res=max(res,i-prefix_sum[needed_sum])
            if total not in prefix_sum:
                prefix_sum[total]=i
        return res
            

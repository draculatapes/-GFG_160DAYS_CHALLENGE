class Solution:
    def countSubarrays(self, arr, k):
        # code here
        prefix_sum=dict()
        prefix_sum[0]=1
        sumi=0
        res=0
        for ele in arr:
            sumi+=ele
            needed=(sumi-k)
            if needed in prefix_sum:
                res+=prefix_sum[needed]
            if sumi in prefix_sum:
                prefix_sum[sumi]+=1
            else:
                prefix_sum[sumi]=1
        return res

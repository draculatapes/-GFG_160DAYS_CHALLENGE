class Solution:
    def subarrayXor(self, arr, k):
        # code here
        
        prefix_xor=dict()
        prefix_xor[0]=1
        cumulative_xor=0
        res=0
        for ele in arr:
            cumulative_xor^=ele
            needed_xor=k^cumulative_xor
            if needed_xor in prefix_xor:
                res+=prefix_xor[needed_xor]
            if cumulative_xor in prefix_xor:
                prefix_xor[cumulative_xor]+=1
            else:
                prefix_xor[cumulative_xor]=1
        return res

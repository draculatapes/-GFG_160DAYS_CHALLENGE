class Solution:
    #Complete the below function
    def countPairs(self,arr, target):
        #Your code here
        freq=dict()
        res=0
        for ele in arr:
            needed=target-ele
            if needed in freq:
                res+=freq[needed]
            if ele not in freq:
                freq[ele]=1
            else:
                freq[ele]+=1
        return res

class Solution:
    def countDistinct(self, arr, k):
        # Code here
        freq=dict()
        i,j=0,0
        res=[]
        while j<len(arr):
            if j-i+1<k:
                if arr[j] in freq:
                    freq[arr[j]]+=1
                else:
                    freq[arr[j]]=1
            if j-i+1==k:
                res.append(len(freq))
                if freq[arr[i]]==1:
                    freq.pop(arr[i])
                else:
                    freq[arr[i]]-=1
                i+=1
            j+=1
        return res

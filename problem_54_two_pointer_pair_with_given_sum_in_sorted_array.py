#Time Complexity-O(N) Space Complexity: O(1)
class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
        res=0
        n=len(arr)
        i,j=0,n-1
        while i<j:
            sumi=arr[i]+arr[j]
            if sumi==target:
                idx=i
                while idx<j and arr[idx]==arr[i]:
                    res+=1
                    idx+=1
                j-=1
            elif sumi>target:
                j-=1
            else:
                i+=1
        return res


#Time Complexity-O(N) Space Complexity: O(N)

class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
        res=0
        freq=dict()
        for ele in arr:
            needed=target-ele
            if needed in freq:
                res+=freq[needed]
            if ele in freq:
                freq[ele]+=1
            else:
                freq[ele]=1
        return res
                


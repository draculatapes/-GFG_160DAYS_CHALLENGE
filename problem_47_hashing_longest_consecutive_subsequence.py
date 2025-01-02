class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        arr.sort()
        streak=arr[0]
        streak=1
        res=0
        for i in range(1,len(arr)):
            if arr[i]==arr[i-1]:
                continue
            if arr[i]!=arr[i-1]+1:
                streak=0
            streak+=1
            res=max(res,streak)
        return res
            

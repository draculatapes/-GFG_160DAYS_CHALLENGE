class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        i,j=0,len(arr)-1
        arr.sort()
        res=0
        while i<j:
            if arr[i]+arr[j]<target:
                res+=(j-i)
                i+=1
            else:
                j-=1
        return res

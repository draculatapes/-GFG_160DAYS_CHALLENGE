class Solution:
    def maxWater(self, arr):
        # code here
        n=len(arr)
        i,j=0,n-1
        res=0
        while i<j:
            while i>0 and arr[i]==arr[i-1]:
                i+=1
            while j<n-1 and arr[j]==arr[j+1]:
                j-=1
            if arr[i]<=arr[j]:
                res=max(res,(j-i)*arr[i])
                i+=1
            else:
                res=max(res,(j-i)*arr[j])
                j-=1
        return res

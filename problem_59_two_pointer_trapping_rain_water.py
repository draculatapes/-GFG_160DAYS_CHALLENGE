class Solution:
    def maxWater(self, arr):
        # code here
        i,j=0,len(arr)-1
        lmax,rmax=arr[0],arr[-1]
        res=0
        while i<j:
            lmax=max(lmax,arr[i])
            rmax=max(rmax,arr[j])
            if arr[i]>arr[j]:
                res+=(rmax-arr[j])
                j-=1
            else:
                res+=(lmax-arr[i])
                i+=1
        return res

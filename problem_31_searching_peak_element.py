class Solution:   
    def peakElement(self,arr):
        # Code here
        n=len(arr)
        low,high=0,n-1
        while low<=high:
            mid=low+(high-low)//2
            if (mid-1<0 or arr[mid-1]<arr[mid]) and (mid+1==n or arr[mid+1]<arr[mid]):
                return mid
            if mid+1<n and (mid-1<0 or arr[mid-1]<arr[mid]) and  arr[mid+1]>arr[mid]:
                low=mid+1
            else:
                high=mid-1
        return -1

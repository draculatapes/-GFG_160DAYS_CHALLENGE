class Solution:
    def kthMissing(self, arr, k):
        # code here
        n=len(arr)
        low,high=0,n-1
        
        while low<=high:
            mid=low+(high-low)//2
            missing_ele=arr[mid]-(mid+1)
            if missing_ele<k:
                low=mid+1
            else:
                high=mid-1
        if low==-1:
            return k
        if low==n:
            return n+k
        return arr[high]+(k-(arr[high]-(high+1)))

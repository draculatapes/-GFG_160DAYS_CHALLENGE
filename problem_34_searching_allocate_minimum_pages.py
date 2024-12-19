class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here
        if k>len(arr):
            return -1
        def isPoss(max_page):
            count=1
            sumi=0
            for i in range(len(arr)):
                sumi+=arr[i]
                if sumi>max_page:
                    count+=1
                    sumi=arr[i]
            return count<=k
        low=max(arr)
        high=sum(arr)
        if len(arr)==k:
            return low
        res=-1

        while low<=high:
            mid=low+(high-low)//2
            if isPoss(mid):
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res

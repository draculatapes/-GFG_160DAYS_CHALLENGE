class Solution:
    def findMin(self, arr):
        #complete the function here
        l,h=0,len(arr)-1
        while l<=h:
            mid=l+(h-l)//2
            if arr[mid]>arr[-1]:
                l=mid+1
            else:
                h=mid-1
        return arr[l]

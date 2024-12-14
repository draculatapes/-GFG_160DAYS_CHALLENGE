class Solution:
    def search(self,arr,key):
        # Complete this function
        target=key
        l,h=0,len(arr)-1
        while l<=h:
            mid=l+(h-l)//2
            if arr[mid]==target:
                return mid
            if arr[mid]>arr[-1]:
                if target>arr[mid] or target<arr[0]:
                    l=mid+1
                else:
                    h=mid-1
            else:
                if target<arr[mid] or target>arr[-1]:
                    h=mid-1
                else:
                    l=mid+1
                    
                    
        return -1

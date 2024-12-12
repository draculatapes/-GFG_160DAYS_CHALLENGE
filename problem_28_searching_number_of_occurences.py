class Solution:
    def countFreq(self, arr, target):
        #code here
        def lowerBound():
            l,h=0,len(arr)-1
            res=0
            while l<=h:
                mid=l+((h-l)//2)
                if arr[mid]>=target:
                    res=mid
                    h=mid-1
                else:
                    l=mid+1
            return res if arr[res]==target else -1
        def upperBound():
            l,h=0,len(arr)-1
            res=-1
            while l<=h:
                mid=l+(h-l)//2
                if arr[mid]<=target:
                    res=mid
                    l=mid+1
                else:
                    h=mid-1
            return res if arr[res]==target else -1
        if (upperBound()==-1 or lowerBound()==-1):
            return 0
        return upperBound()-lowerBound()+1

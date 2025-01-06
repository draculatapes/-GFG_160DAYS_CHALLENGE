class Solution:
    def sumClosest(self, arr, target):
        # code here
        arr.sort()
        i,j=0,len(arr)-1
        min_diff=10**5
        res=[]
        while i<j:
            curr_diff=abs(target-(arr[i]+arr[j]))
            if curr_diff<min_diff:
                min_diff=curr_diff
                res=[arr[i],arr[j]]
            if arr[i]+arr[j]<target:
                i+=1
            else:
                j-=1
        return res
            

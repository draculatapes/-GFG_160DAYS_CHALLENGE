class Solution:
    def subarraySum(self, arr, target):
        # code here
        i,j=0,0
        sumi=0
        while j<len(arr):
            sumi+=arr[j]
            while sumi>target:
                sumi-=arr[i]
                i+=1
            if sumi==target:
                return [i+1,j+1]
            j+=1
        return [-1]

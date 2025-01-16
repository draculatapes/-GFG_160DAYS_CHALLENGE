class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        total=sum(arr)
        prefix_sum=0
        for i in range(len(arr)):
            suffix_sum=total-prefix_sum-arr[i]
            if suffix_sum==prefix_sum:
                return i
            prefix_sum+=arr[i]
        return -1

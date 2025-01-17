class Solution:
    def productExceptSelf(self, arr):
        #code here
        n=len(arr)
        left_mul=[1]*n
        right_mul=[1]*n
        res=[0]*n
        for i in range(n):
            left_mul[i]=arr[i] if i==0 else arr[i]*left_mul[i-1]
        for i in range(n-1,-1,-1):
            right_mul[i]=arr[i] if i==n-1 else arr[i]*right_mul[i+1]
        for i in range(n):
            left=1 if i==0 else left_mul[i-1]
            right=1 if i==n-1 else right_mul[i+1]
            res[i]=left*right
        return res

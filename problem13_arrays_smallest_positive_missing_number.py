class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        arr=set(arr)
        for i in range(1,10**5+1):
            if i not in arr:
                return i
        return n+1

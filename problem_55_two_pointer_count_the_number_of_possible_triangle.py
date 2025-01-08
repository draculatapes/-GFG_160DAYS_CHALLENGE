class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        arr.sort()
        res=0
        n=len(arr)
        for i in range(n-1,1,-1):
            j,k=0,i-1
            while j<k:
                if arr[j]+arr[k]>arr[i]:
                    res+=k-j
                    k-=1
                else:
                    j+=1
                
        return res

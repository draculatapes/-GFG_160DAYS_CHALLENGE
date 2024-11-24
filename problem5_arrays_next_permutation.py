class Solution:
    def nextPermutation(self, arr):
        # code here
        maxi=0 
        i=len(arr)-2
        while i>=0:
            if arr[i]<arr[i+1]:
                break
            i-=1
        if i<0:
            return arr
        for j in range(len(arr)-1,i,-1):
            if arr[j]>arr[i]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
                break
 
        i+=1
        if i==len(arr):
            return arr
        j=len(arr)-1
        while i<j:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            i+=1
            j-=1
        return arr

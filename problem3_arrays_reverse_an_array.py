class Solution:
    def reverseArray(self, arr):
        # code here
        i,j=0,len(arr)-1
        while i<j:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            i+=1
            j-=1

class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        i=-1
        for j in range(len(arr)):
            if arr[j]==0:
                i+=1
                temp=arr[j]
                arr[j]=arr[i]
                arr[i]=temp
        for j in range(len(arr)):
            if arr[j]==1:
                i+=1
                temp=arr[j]
                arr[j]=arr[i]
                arr[i]=temp
        return arr

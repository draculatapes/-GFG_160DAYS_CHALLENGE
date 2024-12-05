#Solution1: Two Pass Solution
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
#Solution:2 Single Pass Solution( Dutch National Flag Algorithm)
class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        low, mid, high = 0, 0, len(arr) - 1
        
        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:  # arr[mid] == 2
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
        
        return arr


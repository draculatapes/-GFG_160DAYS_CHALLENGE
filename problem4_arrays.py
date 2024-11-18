class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        n=len(arr)
        d=d%n
        def reverse(i,j):
            while i<j:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
                j-=1
                i+=1
        reverse(0,n-1)
        reverse(0,n-d-1)
        reverse(n-d,n-1)
        

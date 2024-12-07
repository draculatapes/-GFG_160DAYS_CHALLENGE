class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    def inversionCount(self, arr):
        # Your Code Here
        final_res=[0]
        def merge(arr1,arr2):
            i,j=0,0
            m,n=len(arr1),len(arr2)
            res=[]
            while i<m and j<n:
                if arr1[i]<arr2[j]:
                    res.append(arr1[i])
                    i+=1
                else:
                    res.append(arr2[j])
                    j+=1
            while i<m:
                res.append(arr1[i])
                i+=1
            while j<n:
                res.append(arr2[j])
                j+=1
            return res
        def mergeSort(arr):
            if len(arr)<=1:
                return arr
            mid=len(arr)//2
            arr1=mergeSort(arr[:mid])
            arr2=mergeSort(arr[mid:])
            i,j=0,0
            m,n=len(arr1),len(arr2)
            res=[]
            while i<m and j<n:
                if arr1[i]>arr2[j]:
                    final_res[0]+=(m-i)
                    j+=1
                else:
                    i+=1
            return merge(arr1,arr2)
        mergeSort(arr)
        return final_res[0]

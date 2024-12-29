class Solution:
    def findTriplets(self, arr):
        # Your code here
        res=[]
        index=dict()
        for i in range(len(arr)):
            if arr[i] in index:
                index[arr[i]].append(i)
            else:
                index[arr[i]]=[i]
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                sumi=arr[i]+arr[j]
                if -sumi in index:
                    for curr_index in index[-sumi][::-1]:
                        if curr_index<=j:
                            break
                        res.append([i,j,curr_index])
                
        res.sort()
        return res

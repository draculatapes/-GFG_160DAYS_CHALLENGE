import math
class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        vote=0
        winner1=10**9+1
        n=len(arr)
        res=[]
        required=math.ceil(n/3)
        if required==n//3:
            required+=1
        for ele in arr:
            if vote==0:
                winner1=ele
                vote=1
            else:
                if ele==winner1:
                    vote+=1
                else:
                    vote-=1
        if arr.count(winner1)>=required:
            res.append(winner1)
        winner2=0
        vote=0
        for ele in arr:
            if ele!=winner1:
                if vote==0:
                    winner2=ele
                    vote+=1
                else:
                    if ele==winner2:
                        vote+=1
                    else:
                        vote-=1
        if arr.count(winner2)>=required:
            res.append(winner2)
        res.sort()
        return res

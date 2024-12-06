class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        #code here
        n=len(citations)
        count=[0]*(n+1)
        for cit in citations:
            if cit>=n:
                count[n]+=1
            else:
                count[cit]+=1
        index=n
        num=count[n]
        while num<index:
            index-=1
            num+=count[index]
        return index
        

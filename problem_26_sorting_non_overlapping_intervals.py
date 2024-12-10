class Solution:
    def minRemoval(self, intervals):
        # Code here
        intervals.sort()
        start,end=intervals[0]
        i=1
        res=0
        while i<len(intervals):
            if end>intervals[i][0]:
                res+=1
                if end>intervals[i][1]:
                    start,end=intervals[i]
            else:
                start,end=intervals[i]
            i+=1
        return res

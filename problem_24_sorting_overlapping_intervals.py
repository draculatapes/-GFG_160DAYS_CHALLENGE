class Solution:
    def insertInterval(self, intervals, newInterval):
        # Code here
        i=0
        res=[]
        while (i<len(intervals) and intervals[i][0]<=newInterval[0]):
            res.append(intervals[i])
            i+=1
        if len(res)==0:
            res.append(newInterval)
        else:
            if res[-1][1]>=newInterval[0]:
                res[-1][0]=min(res[-1][0],newInterval[0])
                res[-1][1]=max(res[-1][1],newInterval[1])
            else:
                res.append(newInterval)
        while i<len(intervals):
            if res[-1][1]>=intervals[i][0]:
                res[-1][0]=min(res[-1][0],intervals[i][0])
                res[-1][1]=max(res[-1][1],intervals[i][1])
            else:
                res.append(intervals[i])
            i+=1
        return res

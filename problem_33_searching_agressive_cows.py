
class Solution:

    def aggressiveCows(self, stalls, k):
        if k==1:
            return 0
        stalls.sort()
        def isPoss(req_dis):
            cnt=1
            last_pos=stalls[0]
            for i in range(1,len(stalls)):
                if stalls[i]-last_pos>=req_dis:
                    cnt+=1
                    last_pos=stalls[i]
                if cnt>=k:
                    return True
            return False
        low,high=0,10**6
        res=0
        while low<=high:
            mid=low+(high-low)//2
            if isPoss(mid):
                res=mid
                low=mid+1
            else:
                high=mid-1
        return res
            
        pass

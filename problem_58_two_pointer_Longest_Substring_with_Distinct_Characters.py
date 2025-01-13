class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        i,j=0,0
        present=set()
        res=0
        while j<len(s):
            if s[j] in present:
                while s[i]!=s[j]:
                    present.remove(s[i])
                    i+=1
                i+=1
            else:
                res=max(res,j-i+1)
                present.add(s[j])
            j+=1
        return res

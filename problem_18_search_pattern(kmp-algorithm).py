class Solution:
    def search(self, pat, txt):
        m = len(pat)
        n = len(txt)
        lps = [0] * m
        
        def computeLPS():
            i, l = 1, 0
            while i < m:
                if pat[i] == pat[l]:
                    l += 1
                    lps[i] = l
                    i += 1  
                else:
                    if l != 0:
                        l = lps[l - 1]
                    else:
                        lps[i] = 0
                        i += 1 
        
        computeLPS()
        i, j = 0, 0
        res = []
        
        while i < n:
            if txt[i] == pat[j]:
                i += 1
                j += 1
            if j == m:
                res.append(i - m )
                j = lps[j - 1]
            elif i < n and txt[i] != pat[j]:  
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
            
        return res

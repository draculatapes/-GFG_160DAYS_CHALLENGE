class Solution:
    def findPermutation(self, s):
        # Code here
        output=set()
        n=len(s)
        taken=[False]*n
        def solve(cur_per,taken):
            if len(cur_per)==len(s):
                output.add(cur_per)
            for i in range(len(s)):
                if not taken[i]:
                    taken[i]=True
                    solve(cur_per+s[i],taken)
                    taken[i]=False
        solve("",taken)
        return list(output)

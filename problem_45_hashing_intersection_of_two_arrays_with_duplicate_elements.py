class Solution:
    def intersectionWithDuplicates(self, a, b):
        # code here
        res=set()
        present=set(a)
        for ele in b:
            if ele in present:
                res.add(ele)
        return list(res)

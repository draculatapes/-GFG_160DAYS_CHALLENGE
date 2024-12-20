class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        # code here
        m,n=len(mat),len(mat[0])
        cs,ce=0,n-1
        rs,re=0,m-1
        r,c=0,0
        res=[]
        while cs<ce and rs<re:
            for col in range(cs,ce):
                res.append(mat[rs][col])
            for row in range(rs,re):
                res.append(mat[row][ce])
            for col in range(ce,cs,-1):
                res.append(mat[re][col])
            for row in range(re,rs,-1):
                res.append(mat[row][cs])
            cs+=1
            rs+=1
            re-=1
            ce-=1
        if rs==re:
            for col in range(cs,ce+1):
                res.append(mat[rs][col])
        elif cs==ce:
            for row in range(rs,re+1):
                res.append(mat[row][cs])
        return res

class Solution:
    def isWordExist(self, mat, word):
        #Code here
        
        directions=[[-1,0],[1,0],[0,-1],[0,1]]
        def solve(i,j,w_i,visited):
            if w_i>=len(word):
                return True
            if w_i==len(word)-1 and mat[i][j]==word[w_i]:
                return True
            if mat[i][j]!=word[w_i]:
                return False
            visited[i][j]=True
            for direction in directions:
                i_=i+direction[0]
                j_=j+direction[1]
                if i_>=0 and j_>=0 and i_<m and j_<n and not visited[i_][j_]:
                    res=solve(i_,j_,w_i+1,visited)
                    if res:
                        return True
            visited[i][j]=False
            return False
        m,n=len(mat),len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j]==word[0]:
                    visited=[[False for _ in range(n)] for _ in range(m)]
                    
                    if solve(i,j,0,visited):
                        return True
        return False

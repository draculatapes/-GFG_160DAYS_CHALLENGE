class Solution:
    def nQueen(self, n):
        # code here
        queen_placed=[[False for _ in range(n)] for _ in range(n)]
        def isSafe(row,col):
            for i in range(n):
                if (i!=col and queen_placed[row][i]) or (i!=row and queen_placed[i][col]):
                    return False
            
            i,j=row-1,col-1
            while i>=0 and j>=0:
                if queen_placed[i][j]:
                    return False
                i-=1
                j-=1
            i,j=row+1,col-1
            while i<n and j>=0:
                if queen_placed[i][j]:
                    return False
                i+=1
                j-=1
            
            return True
        visited=[[False for _ in range(n)] for _ in range(n)]
        res=[]
        def dfs(col,seq):
            if col>=n:
                res.append(seq[:])
                return 
            for row in range(n):
                if isSafe(row,col):
                    queen_placed[row][col]=True
                    seq.append(row+1)
                    dfs(col+1,seq)
                    seq.pop()
                queen_placed[row][col]=False
        dfs(0,[])
        return res

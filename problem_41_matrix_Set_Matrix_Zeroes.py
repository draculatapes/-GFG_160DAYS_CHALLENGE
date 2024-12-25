class Solution:
    def setMatrixZeroes(self, mat):
        M=2**31
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    for col in range(len(mat[0])):
                        mat[i][col]=M if mat[i][col]!=0 else 0
                    for row in range(len(mat)):
                        mat[row][j]=M if mat[row][j]!=0 else 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==M:
                    mat[i][j]=0

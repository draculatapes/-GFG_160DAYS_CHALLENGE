
class Solution:
    #Function to find a solved Sudoku. 
    def solveSudoku(self, mat):
        def isSafe(mat,row,col,num):
            for x in range(9):
                if mat[row][x]==num:
                    return False
            for x in range(9):
                if mat[x][col]==num:
                    return False
            startRow=row-(row%3)
            startCol=col-(col%3)
            for i in range(3):
                for j in range(3):
                    if mat[i+startRow][j+startCol]==num:
                        return False
            return True
        def solve(mat,row,col):
            if row==8 and col==9:
                return True
            if col==9:
                row+=1
                col=0
            if mat[row][col]!=0:
                return solve(mat,row,col+1)
            for num in range(1,10):
                if isSafe(mat,row,col,num):
                    mat[row][col]=num
                    if solve(mat,row,col+1):
                        return True
                    mat[row][col]=0
            return False
        solve(mat,0,0)
        

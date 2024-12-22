class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self, mat): 
        # code here
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i>j:
                    continue
                temp=mat[i][j]
                mat[i][j]=mat[j][i]
                mat[j][i]=temp
        i,j=0,len(mat)-1
        while i<j:
            for col in range(len(mat[0])):
                temp=mat[i][col]
                mat[i][col]=mat[j][col]
                mat[j][col]=temp
            i+=1
            j-=1

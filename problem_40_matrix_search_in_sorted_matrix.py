class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchMatrix(self, mat, x): 
    	# code here 
    	m,n=len(mat),len(mat[0])
    	i,j=0,n-1
    	while i<m and j>=0:
    	    if mat[i][j]==x:
    	        return True
    	    if mat[i][j]>x:
    	        j-=1
    	    else:
    	        i+=1
    	return False

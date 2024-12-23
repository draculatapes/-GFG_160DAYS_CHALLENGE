class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchRowMatrix(self, mat, x): 
    	# code here
    	for i in range(len(mat)):
    	    low,high=0,len(mat[0])-1
    	    while low<=high:
    	        mid=low+(high-low)//2
    	        if mat[i][mid]==x:
    	            return True
    	        if mat[i][mid]>x:
    	            high=mid-1
    	        else:
    	            low=mid+1
        return False

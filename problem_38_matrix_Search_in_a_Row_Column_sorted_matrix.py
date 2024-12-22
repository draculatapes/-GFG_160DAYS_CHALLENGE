class Solution:
	def matSearch(self, mat, x):
		# Complete this function
		m,n=len(mat),len(mat[0])
		for i in range(m):
		    low,high=0,n-1
		    while low<=high:
		        mid=low+(high-low)//2
		        if mat[i][mid]==x:
		            return True
		        if mat[i][mid]>x:
		            high=mid-1
		        else:
		            low=mid+1
	    return False

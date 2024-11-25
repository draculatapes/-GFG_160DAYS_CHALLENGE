class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
		curr_prod=1
		i,j=0,0
		res=-sys.maxsize
		while j<len(arr):
		    if arr[j]==0:
		        while i<j:
		            curr_prod//=arr[i]
		            i+=1
		            res=max(res,curr_prod)
		        i+=1
		    else:
		        curr_prod*=arr[j]
		        res=max(curr_prod,res)
            j+=1
            
        while i<j:
            curr_prod//=arr[i]
            res=max(curr_prod,res)
            i+=1
        return max(arr) if res<2 else res

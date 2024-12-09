class Solution:
	def mergeOverlap(self, arr):
		#Code here
		arr.sort()
		res=[arr[0]]
		for i in range(1,len(arr)):
		    if arr[i][0]<=res[-1][1]:
		        res[-1][0]=min(res[-1][0],arr[i][0])
		        res[-1][1]=max(res[-1][1],arr[i][1])
		    else:
		        res.append(arr[i])
		return res

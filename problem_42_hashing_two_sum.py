class Solution:
	def twoSum(self, arr, target):
		# code here
		freq=dict()
		for ele in arr:
		    if ele in freq:
		        freq[ele]+=1
		    else:
		        freq[ele]=1
        for ele in arr:
            needed=target-ele
            if needed==ele:
                if freq[ele]>1:
                    return True
            elif needed in freq:
                return True
        return False

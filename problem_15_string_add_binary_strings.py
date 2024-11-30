class Solution:
	def addBinary(self, s1, s2):
		# code here
		def equateLen(target,original):
		    while len(target)<len(original):
		        target="0"+target
		    return target
		l1,l2=len(s1),len(s2)
	    if l1<l2:
	        s1=equateLen(s1,s2)
	    elif l2<l1:
	        s2=equateLen(s2,s1)
	    rem=0
	    res=""
	    for i in range(len(s1)-1,-1,-1):
	        addition=rem+int(s1[i])+int(s2[i])
	        rem=addition//2
	        res=str(addition%2)+res
	    if rem==1:
	        res="1"+res
	    for i in range(len(res)):
	        if res[i]=="1":
	            return res[i:]
	    return "0"

class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        #code here
  
        n=len(s1)
        string=s2+"$"+s1+s1
        lps=[0]*(3*n+1)
        l=0
        i=1
        while i<len(string):
            if string[i]==string[l]:
                l+=1
                lps[i]=l
                i+=1
            elif l!=0:
                l=lps[l-1]
            else:
                lps[i]=0
                i+=1
            if l==n:
                return True
        return False

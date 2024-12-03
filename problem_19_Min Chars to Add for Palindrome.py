class Solution:
    def minChar(self, s):
        #Write your code here`
        rev=s[::-1]
        n=len(s)
        s+=rev
        lps=[0]*len(s)
        l=0
        i=1
        while i<len(s):
            if s[i]==s[l]:
               l+=1

               lps[i]=l
               i+=1
            elif l!=0:
                l=lps[l-1]
            else:
                lps[i]=0
                i+=1
        return n-lps[-1]

class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        #code here
        if len(s1)!=len(s2):
            return False
        s1=list(s1)
        s2=list(s2)
        s1.sort()
        s2.sort()
        return s1==s2

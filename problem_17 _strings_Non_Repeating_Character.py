class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self,s):
        #code here
        freq=dict()
        for char in s:
            if char in freq:
                freq[char]+=1
            else:
                freq[char]=1
        for char in s:
            if freq[char]==1:
                return char
        return -1

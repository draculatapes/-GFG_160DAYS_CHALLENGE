class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        def isAnagram(target,base):
            if len(target)!=len(base):
                return False
            freqBase=dict()
            for char in base:
                if char in freqBase:
                    freqBase[char]+=1
                else:
                    freqBase[char]=1
            freqTarget=dict()
            for char in target:
                if char in freqTarget:
                    freqTarget[char]+=1
                else:
                    freqTarget[char]=1
            for char in target:
                if char not in freqBase or freqBase[char]!=freqTarget[char]:
                    return False
            return True

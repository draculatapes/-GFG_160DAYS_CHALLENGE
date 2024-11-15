class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        maxi=0
        smaxi=0
        for ele in arr:
            if ele>maxi:
                smaxi=maxi
                maxi=ele
                
            elif ele>smaxi and ele!=maxi:
                smaxi=ele
        return smaxi if smaxi!=0 else -1

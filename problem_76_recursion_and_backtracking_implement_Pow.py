class Solution:
    def power(self, b: float, e: int) -> float:
        # Code Here
        if e==0:
            return 1
        
        if e<1:
            return 1/self.power(b,-e)
        p=self.power(b,e//2)
        if e%2==0:
            return p*p
        return b*p*p

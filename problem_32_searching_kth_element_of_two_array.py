
class Solution:

    def kthElement(self, a, b, k):
        i,j=0,0
        m,n=len(a),len(b)
        ab=list()
        while i<m and j<n:
            if a[i]<b[j]:
                ab.append(a[i])
                i+=1
            else:
                ab.append(b[j])
                j+=1
        while i<m:
            ab.append(a[i])
            i+=1
        while j<n:
            ab.append(b[j])
            j+=1
        return ab[k-1]
                
        pass

class Solution:
    def countTriplets(self, arr, target):
        # code here
        n=len(arr)
        res=0
        for i in range(n-2):
            j,k=i+1,n-1
            while j<k:
                total_sum=arr[i]+arr[j]+arr[k]
                if total_sum==target:
                    ele1=arr[j]
                    ele2=arr[k]
                    cnt1=0
                    cnt2=0
                    while j<=k and arr[j]==ele1:
                        j+=1
                        cnt1+=1
                    while j<=k and arr[k]==ele2:
                        k-=1
                        cnt2+=1
                    if ele1==ele2:
                        res+=(cnt1*(cnt1-1))//2
                    else:
                        res+=(cnt1*cnt2)
                elif total_sum>target:
                    k-=1
                else:
                    j+=1
        return res

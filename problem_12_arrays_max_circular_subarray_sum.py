def circularSubarraySum(arr):
    ##Your code here
    n=len(arr)
    min_sub_sum=sys.maxsize
    max_sub_sum=0
    max_sum=0
    min_sum=0
    total=0

    for ele in arr:
        min_sum+=ele
        max_sum+=ele
        total+=ele
        if max_sum<0:
            max_sum=0
        else:
            max_sub_sum=max(max_sum,max_sub_sum)
        if min_sum>0:
            min_sum=0
        else:
            min_sub_sum=min(min_sub_sum,min_sum)
    return max(max_sub_sum,(total-min_sub_sum))

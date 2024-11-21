from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        profit=0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                profit+=(prices[i+1]-prices[i])
        return profit

class Solution:
    def maximumProfit(self, prices):
        # code here
        selling_price=-1
        profit=0
        for i in range(len(prices)-1,-1,-1):
            if prices[i]>selling_price:
                selling_price=prices[i]
            elif prices[i]<selling_price:
                profit=max(profit,selling_price-prices[i])
        return profit

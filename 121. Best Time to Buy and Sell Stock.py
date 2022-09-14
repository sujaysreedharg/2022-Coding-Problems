class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        maxprofit=0
        while r<len(prices):
            if prices[l]<prices[r]:
                profit= prices[r]-prices[l]
                maxprofit=max(profit,maxprofit)
            else:
                while prices[l]>prices[r]:
                    l+=1
            r+=1
        return maxprofit

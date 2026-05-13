class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        p1 = 0
        p2 = 1
        while p2<len(prices):
            profit = prices[p2]-prices[p1]
            if profit>0:
                maxProfit = max(maxProfit,profit)
            else:
                p1=p2
            p2+=1
        return maxProfit            
        



        
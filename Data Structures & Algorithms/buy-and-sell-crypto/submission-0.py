class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1,0,-1):
            mini = min(prices[:i])
            profit = max(profit,prices[i]-mini)
            print(profit)
        return profit
        



        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0 
        minimumBuy = prices[0]
        for i in range(len(prices)):
            if(prices[i] - minimumBuy > profit): profit = prices[i] - minimumBuy
            if(minimumBuy > prices[i]): minimumBuy = prices[i]
        return profit        
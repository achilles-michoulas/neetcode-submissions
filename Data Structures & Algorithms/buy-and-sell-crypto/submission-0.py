class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        buyPrice = prices[0]

        maxProfit = 0

        for i in range(1, len(prices)):
            sellPrice = prices[i]
        
            if prices[i-1] < buyPrice:
                buyPrice = prices[i-1]
            
            curProfit = sellPrice - buyPrice

            if curProfit > maxProfit:
                maxProfit = curProfit
        
        return maxProfit





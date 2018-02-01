class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if not prices:
            return 0
        
        min_input = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_input:
                min_input = prices[i]
            if prices[i] - min_input > max_profit:
                max_profit = prices[i] - min_input
        return max_profit

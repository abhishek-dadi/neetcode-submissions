class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        for i in range(len(prices) - 1):
            future_max = max(prices[i + 1:])
            if future_max > prices[i]:
                m = max(m, future_max - prices[i])
        return m

        
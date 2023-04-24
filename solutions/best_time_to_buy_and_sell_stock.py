class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_purchase = prices[0]

        for price in prices:
            # set max profit to be highest between the current stored max and price - min_purchase
            max_profit = max(max_profit, price - min_purchase)
            # store the minimum purchase value between the current min_purchase value and price
            min_purchase = min(min_purchase, price)

        return max_profit

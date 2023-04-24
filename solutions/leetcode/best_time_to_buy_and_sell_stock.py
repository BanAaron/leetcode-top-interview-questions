class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_purchase = prices[0]

        # loop through all our possible prices
        for price in prices:
            # as we loop through we update max_profit to be the max between itself and price - min_purchase
            max_profit = max(max_profit, price - min_purchase)

            # we then set min_purchase to be the minimum between itself and the current price in the loop
            min_purchase = min(min_purchase, price)

        return max_profit


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([7, 6, 4, 3, 1]))

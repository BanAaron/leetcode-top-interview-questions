class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_purchase = prices[0]

        for price in prices:
            max_profit = max(max_profit, price - min_purchase)
            min_purchase = min(min_purchase, price)

        return max_profit


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([7, 6, 4, 3, 1]))

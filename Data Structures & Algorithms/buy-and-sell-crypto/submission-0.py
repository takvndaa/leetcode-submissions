class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # input : int arr prices
        # output : int max profit
        # prices[i] is price on ith day
        # buy and sell on days to make the most profit
        # 2 4 2 6 1 8 4 2 1
        # init max profit as 0
        # brute force polynomial time const space compare all 

        max_profit = 0
        i, n = 0, len(prices)

        while i < n:
            j = i
            while j < n:
                max_profit = max(max_profit, prices[j] - prices[i])
                j += 1
            i += 1

        return max_profit 

        
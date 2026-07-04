class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # input : int arr prices 
        # output : int max profit 
        # make two trades for max profit buy sell
        # sim all trades with nested loops and track max profit
        # polynomial time and const space

        res = 0
        i = 0
        while i < len(prices) - 1:
            j = i + 1
            while j < len(prices):
                res = max(prices[j] -  prices[i], res)
                j += 1
            i += 1
        
        return res


        
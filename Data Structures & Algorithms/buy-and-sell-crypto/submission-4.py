class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # input : int arr prices 
        # output : int max profit 
        # make two trades for max profit buy sell
        """     
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
    """
        # use two pointers
        # update max if profit
        # update pointers if loss

        i, j, = 0, 1
        res = 0
        while j < len(prices):
            if prices[j] - prices[i] > 0:
                res = max(res, prices[j] - prices[i])
                j += 1
            else:
                i = j
                j = i + 1
        
        return res

        
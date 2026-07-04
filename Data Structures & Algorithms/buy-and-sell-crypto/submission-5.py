class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # input int arr prices
        # output max_p
        # make buy sell trade to max profit
        # nested loops to sim all trades and track max
        # polynomial order 2 time and const space
        # use two pointers sliding window
        # move r pointer until loss and l pointer to r

        l, r = 0, 1
        res = 0

        while r < len(prices):
            if prices[r] -  prices[l] < 0:
                l = r
                r = l + 1
            else:
                res = max(res, prices[r] - prices[l])
                r += 1
        
        return res
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, max_p, n = 0, 1, 0, len(prices)

        while r < n:
            if prices[r] > prices[l]:
                max_p = max(max_p, prices[r] - prices[l])
                r += 1
            else:
                l = r
                r += 1

        return max_p
            

        
        
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # given int arr nums of len n
        # return arr ans of len 2n
        # ans[i] == nums[i] and ans[i + n] = nums[i]

        n = len(nums)
        ans = [0] * (2 * n)
        for i in range(2 * n):
            ans[i] = nums[i % n]
        
        return ans
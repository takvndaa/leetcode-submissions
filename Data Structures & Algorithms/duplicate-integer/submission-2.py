class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # given int arr nums
        # return bool arr has duplicates
        # brute force nested loops
        # quadratic time, constant space
        # one pass seen hash set solution
        # linear time, linear space

        seen = set()
        n = len(nums)
        for i in range(n):
            if nums[i] in seen:
                return True
            seen.add(nums[i])

        return False
        
        
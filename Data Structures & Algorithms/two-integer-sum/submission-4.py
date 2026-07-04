class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # given int arr nums and int target
        # return int arr [i, j] where nums[i] + nums[j] = target
        # nested loops for all distinct pairs
        # quadratic time and constant space
        # hashing indexes and looking up difference
        # linear time and linear space

        seen = {}
        n = len(nums)

        for i in range(n):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            seen[nums[i]] = i

        
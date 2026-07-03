class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # input : int arr nums and int target
        # output : int arr of indices i and j
        # return i and j such that nums[i] + nums[j] = target
        # for each num loop though arr looking for target - num
        # polynomial time const space
        # for each num look for index of target - num
        # for each num add to hash map mapping to index
        
        indices = {}
        for i in range(len(nums)):
            if target - nums[i] in indices:
                return [indices[target - nums[i]], i]
            indices[nums[i]] = i


        
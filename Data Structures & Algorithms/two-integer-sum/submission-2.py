class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # input int arr nums and int target
        # output int arr of indices i, j
        # return list of two indices with nums that sum to target
        # nested loops checking all sums if target
        # const space and polynomial order 2 time
        # hash indices in single pass 
        # for each el check in difference in map
        # if in map return indices else add to map

        indices = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices:
                return [indices[diff], i]
            indices[n] = i

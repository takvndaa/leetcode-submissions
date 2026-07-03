class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # input : int arr nums
        # output : bool 
        # look for duplicates
        # brute force, constant space and polynomial time
        # optimize with linear space and linear time using hashing

        # init hashset
        seen = set()
        # loop through arr
        for num in nums:      
        # if not in set add else return false
            if num not in seen: seen.add(num)
            else: return True
        # return true
        return False


        
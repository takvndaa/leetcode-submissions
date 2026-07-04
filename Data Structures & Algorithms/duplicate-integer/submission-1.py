class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # input int arra nums
        # output bool
        # look for duplicates in arr
        # nested loops checking rest of arr for each element
        # const space, polynomial order 2 time
        # fast look ups using hash
        # single pass, add elements to seen set
        # return false if already in seen
        # linear space and time

        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False
        
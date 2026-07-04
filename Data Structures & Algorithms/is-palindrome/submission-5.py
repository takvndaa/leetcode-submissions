class Solution:
    def isPalindrome(self, s: str) -> bool:
        # input str s
        # output bool
        # if all alnum chars are in the same order backwards
        # case insensitive
        # strip all non alnum chars
        # reverse str and compare
        # linear space and linear time
        # use two pointers opposite ends
        # skip non alnum chars
        # compare until pointer lap

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False

            l, r = l + 1, r - 1
        
        return True
        
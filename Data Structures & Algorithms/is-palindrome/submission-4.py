class Solution:
    def isPalindrome(self, s: str) -> bool:
        # input str s 
        # output bool 
        # return true uf str s reads the same backwards
        # ignore non alnum chars and letter case
        # strip non alnum chars and reverse str then compare
        # linear space and time
        # two pointer from either end and compare until swap

        l,r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            
            if s[r].lower() != s[l].lower():
                return False
            
            l, r = l + 1, r - 1
        
        return True
        
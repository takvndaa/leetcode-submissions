class Solution:
    def isPalindrome(self, s: str) -> bool:
        # input str s 
        # output bool 
        # return true uf str s reads the same backwards
        # ignore non alnum chars and letter case
        # strip non alnum chars and reverse str then compare
        # linear space and time
        # two pointer from either end and compare until swap

        new_s = ''
        for c in s:
            if c.isalnum():
                new_s += c.lower()
            
        return new_s == new_s[::-1]
        
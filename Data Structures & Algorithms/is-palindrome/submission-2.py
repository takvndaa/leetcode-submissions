class Solution:
    def isPalindrome(self, s: str) -> bool:
        # input : str s 
        # output : bool 
        # return true if str reads the same backwards and forwards
        # ignore non alphanumeric chars
        # case insensitive
        # make new str of only alnum chars
        # reverse  new str and check against new str
        # linear time and space
        # go through str forwards and check if same as backwards
        # use two pointers
        # skip non alnum chars
        # compare chars lowercased

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
                    
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
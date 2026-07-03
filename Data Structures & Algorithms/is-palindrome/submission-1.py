class Solution:
    def isPalindrome(self, s: str) -> bool:
        # input : str s 
        # output : bool 
        # return true if str reads the same backwards and forwards
        # ignore non alphanumeric chars
        # case insensitive
        # reverse str and check linear time and space
        # go through str forwards and check if same as backwards
        # linear time and const space sol
        # use two pointers
        # case insenitive
        
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
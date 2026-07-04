class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # input strs s and t
        # output bool
        # if t has same chars and charcount as s
        # sort and check equality log linear time,linear space
        # use arr for bucket sort
        # increment for s and decrement for t
        # return arr is all 0s
        # const space and linear time
        # use counter and check if counters equal
        # const space linear time

        chars = [0] * 26
        for c in s:
            chars[ord(c) - ord('a')] += 1
        
        for c in t:
            chars[ord(c) - ord('a')] -= 1

        for count in chars:
            if count != 0:
                return False
        
        return True
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

        if len(s) != len(t):
            return False


        counts = [0] * 26
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1

        for count in counts:
            if count != 0:
                return False
        
        return True
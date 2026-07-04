class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # given s and t strs
        # return bool s and t are anagrams
        # ignore case and non alnum chars
        # if len unequal return false
        # check sorted strs equal 
        # linear space and log linear time
        # create counts hash map 
        # linear time and const space due to char limit
        # create counts hash map as arr
        # linear time and const space

        if len(s)  != len(t):
            return False
        
        chars = [0] * 26
        n = len(s)

        for i in range(n):
            sIndex = ord(s[i]) - ord('a')
            tIndex = ord(t[i]) - ord('a')
            chars[sIndex] += 1
            chars[tIndex] -= 1
        
        for i in range(26):
            if chars[i] != 0:
                return False
        
        return True

        
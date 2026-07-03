class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # input : two strs s and t
        # output : bool 
        # check if strs have same chars and chars count
        # for each letter in s check if in t, cont space, linear time
        # sort strs and see if equal, linear space, log linear time
        # use counter, linear space and time

        return Counter(s) == Counter(t)
        
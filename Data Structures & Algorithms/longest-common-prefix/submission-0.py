class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # given list of sts
        # return str longest common prefix or empty str
        # sort strs by len of strings
        # init prefix as shortest word
        # compare to other words
        # update prefix

        strs.sort(key=len)
        prefix = strs[0]

        n = len(strs)

        for i in range(1, n):
            m = len(prefix)
            while m > 0:
                if not strs[i].startswith(prefix):
                    prefix = prefix[:-1]
                    m -= 1
                else:
                    break
            
        return prefix

        
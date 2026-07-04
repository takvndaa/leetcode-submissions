class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # given arr of strs
        # return str of longest prefix
        
        prefix = strs[0]


        for i in range(1, len(strs)):
            j = 0
            while j < len(strs[i]) and j < len(prefix):
                if strs[i][j] != prefix[j]:
                    break
                j += 1
            
            prefix = prefix[:j]    
                


        return prefix

        
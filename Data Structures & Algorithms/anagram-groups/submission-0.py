class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # given arr of strs
        # return arr of strs grouped together as anagrams
        # to check if strs are anagrams use char counter arr
        # change char counter arr to tuple to hash it
        # return list hash table values
        # or use sorted strs as key to hash table
        # n is len of strs and m is len of longest word
        # hash arr method is  m * n time and space
        # sorting method n + mlogm time and m * n space

        groups = {}
        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            if key in groups:
                groups[key].append(strs[i])
            else:
                groups[key] = [strs[i]]
        
        return list(groups.values())



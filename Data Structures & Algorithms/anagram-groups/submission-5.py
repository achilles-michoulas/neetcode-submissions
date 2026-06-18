from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Make empty dictionary
        dict = {}

        # traverse strs,
        for str in strs:
            letterDict = defaultdict(int)
            
            for char in str:
                letterDict[char] += 1

            key = tuple(sorted(letterDict.items()))

            if key in dict:
                dict[key].append(str)
            else:
                dict[key] = [str]
        
        return list(dict.values())
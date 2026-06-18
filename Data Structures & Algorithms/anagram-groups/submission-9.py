from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for str in strs:
            key = ''.join(sorted(str))

            if key in dict:
               dict[key].append(str) 
            else:
                dict[key] = [str]
        
        return list(dict.values())
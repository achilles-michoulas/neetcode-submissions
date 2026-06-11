class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for string in strs:
            charCounts = {}
            
            for char in string:
                charCounts[char] = charCounts.get(char, 0) + 1


            key = tuple(sorted(charCounts.items()))

            if key in groups:
                groups[key].append(string)
            else:
                groups[key] = [string]

        return list(groups.values())
            


        
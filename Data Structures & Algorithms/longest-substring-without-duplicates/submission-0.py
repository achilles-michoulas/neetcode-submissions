class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        L = 0

        window = set()

        for R in range(len(s)):
            if s[R] in window:
                found = False
                while not found:
                    if s[L] == s[R]:
                        found = True
                    else:
                        window.remove(s[L])
                    L += 1
                    
            else:
                window.add(s[R])
                longest = max(longest, len(window))
        
        return longest



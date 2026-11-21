class Solution:

    def encode(self, strs: List[str]) -> str:
        codedStr = ""
        for s in strs:
            codedStr += str(len(s))
            codedStr += "#"
            codedStr += s
        
        return codedStr

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            i = j + 1
            end = i + length

            res.append(s[i:end])
            i = end
        
        return res

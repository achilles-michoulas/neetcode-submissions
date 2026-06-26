class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        output = 0

        for i in nums:
            if i == 1:
                current += 1
                
                if current > output:
                    output = current
                
            else:
                current = 0
        
        return output

        
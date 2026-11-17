class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        output = []

        for i in range(len(nums) - 2):
            if i != 0:
                if sortedNums[i] == sortedNums[i-1]:
                    continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = sortedNums[i] + sortedNums[j] + sortedNums[k]

                if total == 0:
                    output.append([sortedNums[i], sortedNums[j], sortedNums[k]])
                    
                    j += 1
                    while j < k and sortedNums[j - 1] == sortedNums[j]:
                        j += 1
                    
                    k -= 1
                    while j < k and sortedNums [k + 1] == sortedNums[k]:
                        k -= 1

                elif total < 0:
                    j += 1
                    while j < k and sortedNums[j - 1] == sortedNums[j]:
                        j += 1

                elif total > 0:
                    k -= 1
                    while j < k and sortedNums [k + 1] == sortedNums[k]:
                        k -= 1
        
        return output
                
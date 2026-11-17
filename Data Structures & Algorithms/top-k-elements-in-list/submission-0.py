class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        
        for num in nums:
            if num in freq:
                freq[num] = freq[num] + 1
            else:
                freq[num] = 1
        
        sortedKeys = sorted(freq.keys(), key = lambda x: freq[x], reverse=True)

        return sortedKeys[0:k]


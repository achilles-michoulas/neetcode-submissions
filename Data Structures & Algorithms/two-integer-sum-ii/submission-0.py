class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1

        total = numbers[low] + numbers[high]
       
        while total != target:
            total = numbers[low] + numbers[high]

            if total > target:
                high = high - 1
            elif total < target:
                low = low + 1
        
        return [low + 1, high + 1]
            

        
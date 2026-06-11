class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous = {}

        for index, num in enumerate(nums):
            difference = target - num
            
            if difference in previous:
                first = previous[difference]
                second = index
                return [first, second]
            else:
                previous[num] = index
            

            

        
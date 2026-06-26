class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxNum = arr[-1]
        
        for i in range(len(arr) - 1, -1, -1):
            swapNum = maxNum
            maxNum = max(maxNum, arr[i])
            arr[i] = swapNum
            
        arr[-1] = -1

        return arr

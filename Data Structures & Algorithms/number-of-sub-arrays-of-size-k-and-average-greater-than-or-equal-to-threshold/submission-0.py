class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        runningTotal = 0
        result = 0

        for R in range(len(arr)):
            if (R - L) > k - 1:
                runningTotal -= arr[L]
                L += 1
            
            runningTotal += arr[R]
            
            average = runningTotal / k

            if (R - L) == k - 1 and average >= threshold:
                result += 1
        
        return result
        



            


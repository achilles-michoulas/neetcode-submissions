class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # sliding window O(n) time instead of O(n*k)
        hashSet = set()
        L = 0

        for R in range(len(nums)):
            if (R - L) > k:
                hashSet.remove(nums[L])
                L += 1
            if nums[R] in hashSet:
                return True
            else:
                hashSet.add(nums[R])
        
        return False





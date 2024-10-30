# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Calculate LIS for each element
        lis = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)
        
        # Calculate LDS for each element
        lds = [1] * n
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    lds[i] = max(lds[i], lds[j] + 1)
        
        # Calculate the maximum mountain array length
        max_mountain_len = 0
        for i in range(1, n - 1): 
            if lis[i] > 1 and lds[i] > 1: 
                max_mountain_len = max(max_mountain_len, lis[i] + lds[i] - 1)
    
        return n - max_mountain_len

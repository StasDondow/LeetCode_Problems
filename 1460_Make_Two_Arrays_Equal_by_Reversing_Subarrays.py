# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays 

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if set(target) != set(arr):
            return False
        
        for num in set(target):
            if target.count(num) != arr.count(num):
                return False
        
        return True 

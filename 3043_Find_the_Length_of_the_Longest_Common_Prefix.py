# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def common_prefix_length(str1, str2):
            min_len = min(len(str1), len(str2))
            i = 0
            while i < min_len and str1[i] == str2[i]:
                i += 1
            return i

        arr1 = sorted(map(str, arr1))
        arr2 = sorted(map(str, arr2))

        max_prefix_length = 0
        i, j = 0, 0

        while i < len(arr1) and j < len(arr2):
            prefix_len = common_prefix_length(arr1[i], arr2[j])
            max_prefix_length = max(max_prefix_length, prefix_len)

            if arr1[i] < arr2[j]:
                i += 1
            else:
                j += 1

        return max_prefix_length

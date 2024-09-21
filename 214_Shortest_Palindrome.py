# https://leetcode.com/problems/shortest-palindrome

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s or s == s[::-1]:
            return s

        concat = s + '#' + s[::-1]
        
        n = len(concat)
        lps = [0] * n  
        for i in range(1, n):
            j = lps[i - 1]
            while j > 0 and concat[i] != concat[j]:
                j = lps[j - 1]
            if concat[i] == concat[j]:
                j += 1
            lps[i] = j

        longest_palindromic_prefix_len = lps[-1]
        
        to_add = s[longest_palindromic_prefix_len:][::-1]
        
        return to_add + s

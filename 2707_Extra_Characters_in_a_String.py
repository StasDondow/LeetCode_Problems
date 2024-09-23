# https://leetcode.com/problems/extra-characters-in-a-string

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [n] * (n + 1)
        dp[0] = 0 

        word_set = set(dictionary) 

        for i in range(n):
            dp[i + 1] = min(dp[i + 1], dp[i] + 1)
            for word in dictionary:
                if s.startswith(word, i):
                    dp[i + len(word)] = min(dp[i + len(word)], dp[i])
        return dp[n]

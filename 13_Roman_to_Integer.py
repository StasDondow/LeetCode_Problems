# https://leetcode.com/problems/roman-to-integer/description/

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        prev = s[len(s) - 1]
        result = d[prev]
        for i in range(len(s) - 2, -1, -1):
            current = s[i]
            if list(d.keys()).index(current) < list(d.keys()).index(prev):
                result -= d[current]
            else:
                result += d[current]
            prev = current
        return result

# https://leetcode.com/problems/baseball-game

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        scores = []
        
        for o in operations:
            
            try:
                scores.append(int(o))
                continue
            except ValueError: pass
            
            if o == "+" and len(scores) > 1:
                scores.append(scores[-1] + scores[-2])
            
            elif o == "D" and len(scores) > 0:
                scores.append(scores[-1] * 2)
            
            elif o == "C" and len(scores) > 0:
                scores.pop()

        return sum(scores)

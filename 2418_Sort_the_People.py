# https://leetcode.com/problems/sort-the-people

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(1, len(names)):
            max_value = max(heights[i:])
            max_index = heights.index(max_value)
            if heights[i-1] < heights[max_index]:
                names[i-1], names[max_index] = names[max_index], names[i-1]
                heights[i-1], heights[max_index] = heights[max_index], heights[i-1]
        return names
